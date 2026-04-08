---
id: repo-fetched-ai-hands-on-085528
type: knowledge
owner: OA
registered_at: 2026-04-04T15:46:23.948473
tags: ["auto-cloned", "AI", "Deep Learning", "PyTorch", "oa-assimilated", "premium-repo"]
---

# FETCHED_ai-hands-on_085528

## Assimilation Report
This repository is a comprehensive, hands-on educational guide designed to teach AI engineering from fundamental principles to advanced LLM systems. It covers topics ranging from linear algebra and PyTorch basics to Transformers, RAG, and deep neural network construction.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# AI Engineering: Hands-on
![Stars](https://img.shields.io/github/stars/Ramakm/ai-hands-on?style=flat-square)
![Forks](https://img.shields.io/github/forks/Ramakm/ai-hands-on?style=flat-square)
![PRs](https://img.shields.io/github/issues-pr/Ramakm/ai-hands-on?style=flat-square)
![Issues](https://img.shields.io/github/issues/Ramakm/ai-hands-on?style=flat-square)
![Contributors](https://img.shields.io/github/contributors/Ramakm/ai-hands-on?style=flat-square)
![License](https://img.shields.io/github/license/Ramakm/ai-hands-on?style=flat-square)
<img width="2000" height="600" alt="image" src="https://github.com/user-attachments/assets/0c161d9a-3227-4dd7-a416-ad97bc9742a9" />

A complete, hands-on guide to becoming an AI Engineer.

This repository is designed to help you learn AI from first principles, build real neural networks, and understand modern LLM systems end-to-end.
You'll progress through math, PyTorch, deep learning, transformers, RAG, and OCR — with clean, intuitive Jupyter notebooks guiding you at every step.

Whether you're a beginner or an engineer levelling up, this repo gives you the clarity, structure, and intuition needed to build real AI systems.

#### ⭐ Star This Repo

If you learn something useful, a star is appreciated.

## Repository Structure

### 1. Math Fundamentals
- Math functions, derivatives, vectors, and gradients
- Matrix operations and linear algebra
- Probability and statistics

### 2. PyTorch Basics
- Creating and manipulating tensors
- Matrix multiplication, transposing, and reshaping
- Indexing, slicing, and concatenating tensors
- Special tensor creation functions

### 3. Neural-Network(NN)
- Building neurons, layers, and networks from scratch
- Normalization techniques (RMSNorm)
- Activation functions
- Optimizers (Adam, Muon) and learning rate decay

### 4. Transformers
- Attention and self-attention mechanisms
- Multi-head attention
- Decoder-only transformer architecture

### 5. Retrieval-Augmented Generation (RAG)
- Building RAG pipelines end to end
- Indexing, retrieval, chunking strategies
- Integrations with embedding models and vector stores

### 6. Optical Character Recognition (OCR)
- OCR pipeline and utilities
- Preprocessing images and extracting text

## Books

Recommended reading to deepen your understanding (not included):

- `AI Engineering` by Chip Huyen
- `Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow` by Aurélien Géron
- `Deep Learning` by Ian Goodfellow, Yoshua Bengio, and Aaron Courville
- `The Elements of Statistical Learning` by Trevor Hastie, Robert Tibshirani, and Jerome Friedman
- `Neural Networks and Deep Learning` by Michael Nielsen
- `SQL Cookbook` by Anthony Molinaro

For more books in AI/ML, I have created another repo for this [Check Here](https://github.com/Ramakm/AI-ML-Book-References.git). I will be adding lot more in coming days/months. If you are interested to read book, go check this repo out.

## Learning Path

For a recommended step-by-step progression through the materials, see the Learning Path:

- `Start_here/learning_path.md`

## Requirements

Install dependencies with:
```bash
pip install -r requirements.txt
```

Some subfolders (for example `5.RAG/` and `6.OCR/`) include their own `requirements.txt` with additional dependencies.

## Usage

Recommended workflow:

1. Open Jupyter in the project root:
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```
2. Work through notebooks in order:
   - `1.Math/`
   - `2.PyTorch/`
   - `3.Neural-Network(NN)/`
   - `4.Transformer/`

3. Folder to run separately:
   - `5.RAG/`
   - `6.OCR/`
  
4. Resources
5. Basic ML Model Implementation (Supervised + Un-supervised + RL)
   - `1.Linear Regression`
   - `2.Logistic Regression`
   - `3.Decision Tree Model`
   - `4.Naive Bayes Classification`
  
## Machine Learning Frameworks

| Tool         | Category          | Link                                                                                     |
| ------------ | ----------------- | ---------------------------------------------------------------------------------------- |
| Scikit-learn | Traditional ML    | [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)                     |
| XGBoost      | Gradient Boosting | [https://xgboost.ai/](https://xgboost.ai/)                                               |
| LightGBM     | Gradient Boosting | [https://lightgbm.readthedocs.io/en/stable/](https://lightgbm.readthedocs.io/en/stable/) |
| CatBoost     | Gradient Boosting | [https://catboost.ai/](https://catboost.ai/)                                             |


## GEN AI References

| Resource                              | Focus Area             | Link                                                                                                                                                                   |
| ------------------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Microsoft Generative AI for Beginners | Intro to GenAI         | [https://github.com/microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)                                                   |
| Generative AI for Everyone            | Non-technical overview | [https://www.coursera.org/learn/generative-ai-for-everyone](https://www.coursera.org/learn/generative-ai-for-everyone)                                                 |
| Building Blocks of Generative AI      | Conceptual foundations | [https://shriftman.substack.com/p/the-building-blocks-of-generative](https://shriftman.substack.com/p/the-building-blocks-of-generative)                               |
| The Illustrated Transformer           | Transformers           | [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)                                                             |
| LLMs Explained Briefly                | LLM basics video       | [https://www.youtube.com/watch?v=LPZh9BOjkQs](https://www.youtube.com/watch?v=LPZh9BOjkQs)                                                                             |
| Intro to LLMs                         | LLM overview video     | [https://www.youtube.com/watch?v=zjkBMFhNj_g](https://www.youtube.com/watch?v=zjkBMFhNj_g)                                                                             |
| Understanding LLMs                    | Deep dive              | [https://magazine.sebastianraschka.com/p/understanding-large-language-models](https://magazine.sebastianraschka.com/p/understanding-large-language-models)             |
| Visual Guide to Reasoning LLMs        | Reasoning models       | [https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-reasoning-llms)         |
| Understanding Reasoning LLMs          | Reasoning theory       | [https://magazine.sebastianraschka.com/p/understanding-reasoning-llms](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)                           |
| Understanding Multimodal LLMs         | Vision + text models   | [https://magazine.sebastianraschka.com/p/understanding-multimodal-llms](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)                         |
| Visual Guide to MoE                   | Mixture of Experts     | [https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts) |
| Finetuning LLMs                       | Model training         | [https://magazine.sebastianraschka.com/p/finetuning-large-language-models](https://magazine.sebastianraschka.com/p/finetuning-large-language-models)                   |
| How Transformer LLMs Work             | Architecture           | [https://www.deeplearning.ai/short-courses/how-transformer-llms-work/](https://www.deeplearning.ai/short-courses/how-transformer-llms-work/)                           |
| Build GPT from Scratch                | Hands-on               | [https://www.youtube.com/watch?v=kCc8FmEb1nY](https://www.youtube.com/watch?v=kCc8FmEb1nY)                                                                             |
| LLM Course (GitHub)                   | Structured learning    | [https://github.com/mlabonne/llm-course](https://github.com/mlabonne/llm-course)                                                                                       |
| LLM Course (Hugging Face)             | Practical LLMs         | [https://huggingface.co/learn/llm-course/chapter1/1](https://huggingface.co/learn/llm-course/chapter1/1)                                                               |
| Awesome LLM Apps                      | Project ideas          | [https://github.com/Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)                                                                   |
| How RAG Enhances LLMs                 | RAG                    | [https://awesomeneuron.substack.com/p/how-rag-enhances-llms-a-step-by-step](https://awesomeneuron.substack.com/p/how-rag-enhances-llms-a-step-by-step)                                                       |
| Visual Guide to AI Agents             | AI Agents              | [https://awesomeneuron.substack.com/p/a-visual-guide-to-ai-agents](https://awesomeneuron.substack.com/p/a-visual-guide-to-ai-agents)                                        |

## Contributing

Contributions are welcome!

Please ensure:

- Notebooks are clean (Restart & Run All before committing)
- Existing structure & naming conventions are followed
- PRs are focused, readable, and documented
- In folders like RAG and OCR, please maintain the cleaned structure part
- If you want to add something new folders, make it proper structure way.

## License

- This project is licensed under the MIT License. See `LICENSE` for details.

## Connect with me

[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/techwith_ram)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/techwith.ram)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ramakm)


```

### File: requirements.txt
```txt
numpy>=1.20.0
matplotlib>=3.3.0
# torch>=2.0.0


```

### File: DEEP_KNOWLEDGE.md
```md
# Deep Matrix Profile: FETCHED_ai-hands-on_085528

# Deep Knowledge Report for CyberSec RAG Analyzer

## Overview

This repository is designed as an educational tool to teach AI engineering from fundamental principles to advanced LLM systems. It covers a wide range of topics including linear algebra, PyTorch basics, and deep neural network construction, with a focus on implementing a Retrieval-Augmented Generation (RAG) system for cybersecurity analysis.

## Architectural Patterns

### 1. **Modular Structure**
   - The repository is modular, with distinct directories (`5.RAG`, `6.OCR`) each serving specific purposes.
     - **`5.RAG`**: Contains the core RAG system components such as embedding generation, context retrieval, and answer generation.
     - **`6.OCR`**: Implements an OCR API to extract text from images.

### 2. **Streamlit Web Interface**
   - The `app.py` file in `5.RAG/src` sets up a Streamlit web application for user interaction.
     - **Page Configuration**: Custom CSS is used to enhance the UI, making it more visually appealing and user-friendly.
     - **Components**:
       - **Load Embedding Model**: Uses `SentenceTransformer` from Hugging Face to generate embeddings.
       - **Retrieve Context**: Utilizes FAISS for efficient similarity search among document chunks.
       - **Generate Answer**: Employs BART model for context-aware question answering.

### 3. **FAISS Indexing**
   - The `create_embeddings.py` script in `5.RAG/src` generates a FAISS index to store and query embeddings efficiently.
     - **Text Chunking**: Texts are chunked into smaller segments (400 words) for better indexing.
     - **Embedding Generation**: Uses `SentenceTransformer` to generate embeddings for each text segment.

### 4. **BART Model for Answer Generation**
   - The `generate_answer.py` script in `5.RAG/src` leverages the BART model for generating answers based on context and questions.
     - **Contextual Understanding**: Context is provided as input to the BART model, which generates a response.
     - **Error Handling**: Implements caching mechanisms (`lru_cache`) to optimize repeated model loading.

### 5. **PDF Text Extraction**
   - The `extract_text.py` script in `6.OCR/src` uses PyMuPDF (fitz) to extract text from PDF files.
     - **Processing Pipeline**: Converts raw PDFs into text files, which can then be used by the RAG system.

## Core Algorithms and Primary Mechanisms

### 1. **Embedding Generation**
   - **SentenceTransformer**:
     - Uses `all-MiniLM-L6-v2` model to generate dense vector representations of text chunks.
     - Ensures that the model is loaded on CPU for stability and efficiency.
   
   ```python
   model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')
   ```

### 2. **FAISS Indexing**
   - **Index Creation**:
     - Creates a FAISS index to store embeddings, enabling fast similarity searches.
     - Uses `faiss.IndexFlatL2` for L2 distance-based indexing.

   ```python
   index = faiss.IndexFlatL2(dimension)
   index.add(embeddings)
   ```

### 3. **Context Retrieval**
   - **Similarity Search**:
     - Retrieves relevant context chunks based on the input query using FAISS.
     - Reranks results with `rerank_by_mnli` to improve relevance.

   ```python
   relevant_chunks = get_relevant_chunks(query, index)
   reranked_chunks = rerank_by_mnli(relevant_chunks)
   ```

### 4. **Answer Generation**
   - **BART Model**:
     - Uses BART for generating context-aware answers.
     - Implements caching to avoid repeated model loading and improve performance.

   ```python
   response = answer_with_context(context, question)
   ```

### 5. **OCR API**
   - **Image Processing**:
     - Utilizes OpenCV and PIL for image processing and text extraction from images.
   
   ```python
   img_array = np.frombuffer(http_response.content, np.uint8)
   img = cv.imdecode(img_array, cv.IMREAD_COLOR)
   ```

### 6. **Gemini API Integration**
   - **Invoice Data Extraction**:
     - Uses Gemini to extract structured data from raw invoice text.
     - Formats the output according to a predefined JSON schema.

   ```python
   response = model.generate_content(prompt)
   ```

## Conclusion

This repository provides a comprehensive framework for building an RAG system, integrating advanced NLP models and efficient indexing techniques. The modular design ensures that each component can be understood and modified independently, making it suitable for both educational purposes and practical applications in cybersecurity analysis.

---

**Note**: This report is based on the provided source code snippets and does not include any external dependencies or specific configurations beyond what was included in the code samples.
```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for ai_hands_on
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

