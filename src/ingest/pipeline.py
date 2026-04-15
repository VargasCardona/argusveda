import os

from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.stores import InMemoryStore
from langchain_classic.retrievers.parent_document_retriever import (
    ParentDocumentRetriever,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter

from ..core.config import (
    CHROMA_PATH,
    STORE_PATH,
    DATA_PATH,
    CHILD_SPLITTER_CHUNK_SIZE,
    PARENT_SPLITTER_CHUNK_SIZE,
)
from ..core.embeddings import embeddings


def create_retriever() -> ParentDocumentRetriever:
    vectorstore = Chroma(
        collection_name="metasploitable_vulnerabilities",
        embedding_function=embeddings,
        persist_directory=str(CHROMA_PATH),
    )

    store = InMemoryStore()

    parent_splitter = RecursiveCharacterTextSplitter(
        chunk_size=PARENT_SPLITTER_CHUNK_SIZE
    )
    child_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHILD_SPLITTER_CHUNK_SIZE
    )

    retriever = ParentDocumentRetriever(
        vectorstore=vectorstore,
        docstore=store,
        child_splitter=child_splitter,
        parent_splitter=parent_splitter,
    )

    return retriever


def ingest_vulnerabilities(data_path=None, retriever=None):
    if data_path is None:
        data_path = DATA_PATH

    if retriever is None:
        retriever = create_retriever()

    documents = []
    for file in os.listdir(data_path):
        if file.endswith(".md"):
            with open(os.path.join(data_path, file), "r") as f:
                content = f.read()
                doc = Document(page_content=content, metadata={"source": file})
                documents.append(doc)

    retriever.add_documents(documents, ids=None)
    print(
        f"[ARGUSVEDA] Base de conocimientos indexada. {len(documents)} registros cargados."
    )

    return retriever
