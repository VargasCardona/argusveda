# LMP Assistant (Language Model Pentester)
![Repo Size](https://img.shields.io/github/repo-size/VargasCardona/language-model-pentester?style=for-the-badge)
![License](https://img.shields.io/github/license/VargasCardona/language-model-pentester?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/VargasCardona/language-model-pentester?style=for-the-badge)

### A Context-Aware RAG Chain for Ethical Hacking & Vulnerability Analysis

**LMP Assistant** is a specialized cybersecurity tool built with **LangChain**. It leverages Retrieval-Augmented Generation (RAG) to bridge the gap between raw network scan results and actionable security intelligence. By connecting a specialized knowledge base to a sequence of logical processors, LMP assists security researchers in identifying exploits and remediation steps for vulnerable targets like **Metasploitable**.

---

## Architecture: The "1+4" Chain

This project implements a strictly linear **LCEL (LangChain Expression Language)** pipeline.

### 1. The Retriever (Knowledge Base)
* **Type:** `VectorStoreRetriever`
* **Function:** Performs semantic search across an indexed database of **CVEs (Common Vulnerabilities and Exposures)**, **Exploit-DB** entries, and **Rapid7** documentation.
* **Use Case:** When an open port or service version is detected (e.g., `vsftpd 2.3.4`), the retriever fetches the specific exploit technicalities.

---

### 2. The 4 Runnables (The Pipeline)

The system processes data through four distinct **Runnables** to transform raw documents into a structured pentesting plan:

1.  **Context Compressor (`Runnable`):** * Takes the raw documents from the Retriever and strips away irrelevant metadata.
    * Ensures only the technical exploit payload or vulnerability description is passed forward.
    
2.  **Strategic Prompt Template (`Runnable`):** * A custom `ChatPromptTemplate` that structures the instructions.
    * It injects a "System Message" enforcing ethical boundaries and formatting the retrieved context into a query the LLM can understand.

3.  **Inference Engine (`LLM Runnable`):** * The core Model (e.g., GPT-4 or Llama-3).
    * It reasons through the provided context to suggest specific `msfconsole` commands or manual verification steps.

4.  **Security Report Parser (`OutputParser Runnable`):** * Final stage that cleans the LLM output.
    * Converts the text into a structured **Markdown** report including: *Vulnerability Name*, *Risk Level*, *Exploit Command*, and *Mitigation Steps*.

---

## Demonstration: Metasploitable Environment

This assistant is designed to be tested against **Metasploitable 2/3** in an isolated lab environment. 

**Workflow Example:**
1.  **Input:** User provides an Nmap scan output.
2.  **Process:** LMP identifies the `backdoor` vulnerability in the FTP service via the **Retriever**.
3.  **Output:** LMP generates the specific Metasploit module path and the required `RHOSTS` configuration.



## Ethical Disclosure & Disclaimer

**LMP Assistant** is intended for **Authorized Ethical Hacking** and educational purposes only. 
* **Scope:** Only use this tool against assets you own or have explicit written permission to test.
* **Safety:** The system is designed to run in air-gapped or isolated virtual networks.
* **Compliance:** The developers are not responsible for any misuse or damage caused by this tool.



## Technical Stack
* **Framework:** LangChain (LCEL)
* **Storage:** FAISS / ChromaDB
* **Language:** Python 3.10+

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
