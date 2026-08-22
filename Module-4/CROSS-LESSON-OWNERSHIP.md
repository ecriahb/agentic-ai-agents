# Module 4 — Cross-Lesson Ownership Map

The purpose of this file is to prevent concept duplication while preserving the teaching sequence.

| Lesson | Canonical responsibility | Should not re-teach deeply |
|---|---|---|
| 01 | Why external knowledge/retrieval is needed | embedding math, vector DB implementation |
| 02 | What an embedding is; representation, vector semantics, dimensions, embedding vs generation | detailed text-to-vector pipeline, similarity formulas |
| 03 | How text travels through an embedding pipeline; tokenization at high level; batch/single encoding; shape; query/document compatibility | repeating the full definition of embeddings |
| 04 | Similarity search mechanics, nearest neighbors, Top-K, ranking, brute-force search | detailed metric math |
| 05 | Metric theory: cosine, L2, normalization, library semantics, metric configuration | Top-K/retrieval mechanics already taught in Lesson 04 |
| 06 | Vector database/index concepts, exact vs ANN, persistence, metadata, lifecycle | product-specific Chroma/FAISS code |
| 07 | Chroma/FAISS hands-on implementation and tool comparison | general vector DB theory |
| 08 | Chunking strategy and retrieval-unit design | basic embedding definition |
| 09 | Metadata schema/filtering and source-aware retrieval | generic vector DB definitions |
| 10 | End-to-end indexing and query lifecycle | deep metric theory |
| 11 | DevOps knowledge-base implementation | generic vector DB introduction |
| 12 | Integrated local semantic-search project | re-teaching all individual concepts from scratch |

## Boundary rule

A later lesson may mention an earlier concept briefly when needed for implementation, but should link/reference the canonical lesson instead of reproducing the complete explanation.

## Module 4 Mental Progression

```text
Why retrieval?
   ↓
What is an embedding?
   ↓
How is text encoded?
   ↓
How are vectors compared/ranked?
   ↓
Which metric semantics apply?
   ↓
How do we store/index vectors efficiently?
   ↓
How do Chroma/FAISS implement it?
   ↓
How do we chunk/filter/index real documents?
   ↓
How do we build a DevOps knowledge base?
   ↓
How do we integrate everything into a searchable application?
```
