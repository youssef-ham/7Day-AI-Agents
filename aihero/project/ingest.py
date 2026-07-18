import io
import zipfile
import requests
import frontmatter

from minsearch import Index


def read_repo_data(repo_owner, repo_name):
    url = f"https://codeload.github.com/{repo_owner}/{repo_name}/zip/refs/heads/main"

    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception(
            f"Failed to download repository: {resp.status_code}"
        )

    repository_data = []

    zf = zipfile.ZipFile(io.BytesIO(resp.content))

    for file_info in zf.infolist():

        filename = file_info.filename.lower()

        if not (
            filename.endswith(".md")
            or filename.endswith(".mdx")
        ):
            continue

        try:
            with zf.open(file_info) as f:
                content = (
                    f.read()
                    .decode(
                        "utf-8",
                        errors="ignore",
                    )
                )

                post = frontmatter.loads(content)
                data = post.to_dict()

                _, filename_repo = file_info.filename.split(
                    "/",
                    maxsplit=1,
                )

                data["filename"] = filename_repo

                repository_data.append(data)

        except Exception as e:
            print(e)

    return repository_data


def chunk_text(text, size=800):
    return [
        text[i:i + size]
        for i in range(0, len(text), size)
    ]


def chunk_documents(docs):

    chunks = []

    for doc in docs:

        content = doc.get("content", "")

        if not content:
            continue

        pieces = chunk_text(content, size=800)

        for piece in pieces:

            chunks.append(
                {
                    "title": doc.get(
                        "title",
                        "",
                    ),
                    "sidebarTitle": doc.get(
                        "sidebarTitle",
                        "",
                    ),
                    "name": doc.get(
                        "name",
                        "",
                    ),
                    "description": doc.get(
                        "description",
                        "",
                    ),
                    "filename": doc.get(
                        "filename",
                        "",
                    ),
                    "content": piece,
                }
            )

    return chunks


def index_data(
    repo_owner,
    repo_name,
    filter=None,
):

    docs = read_repo_data(
        repo_owner,
        repo_name,
    )

    if filter is not None:
        docs = [
            doc
            for doc in docs
            if filter(doc)
        ]

    docs = chunk_documents(docs)

    print(
        f"Indexed {len(docs)} chunks."
    )

    index = Index(
        text_fields=[
            "title",
            "sidebarTitle",
            "name",
            "description",
            "content",
            "filename",
        ]
    )

    index.fit(docs)

    return index