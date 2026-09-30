from smolagents import Tool
from langchain_community.retrievers import BM25Retriever
from app.dataset.knowledgebase import docs_processed

class RetreiverTool(Tool):
    name="retriever"
    description="Uses semantic search to retrieve the parts of transformers documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question."
        }

    }
    output_type = "string"


    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_documents(docs, k=10)

    def forward(self, query:str)->str:
        """Execute the retrieval based on the provided query."""

        assert isinstance(query, str), "Query must be a string."

        docs = self.retriever.invoke(query)

        return "\nRetrieved documents:\n" + " ".join(
            [f"\n\n=====Document {str(i)} ======\n" + doc.page_content
            for i, doc in enumerate(docs)
            ]
        )

retreiver_tool = RetreiverTool(docs_processed)
    