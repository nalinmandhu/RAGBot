## Introduction

# Objective
The study aims to explore whether Large Language Models (LLMs) can reason effectively without relying on prompting techniques or instruction tuning. Instead of refining prompts, the research investigates an alternative method—modifying the decoding process—to elicit reasoning capabilities that are inherently present in LLMs. The goal is to assess the intrinsic reasoning abilities of LLMs in a task-agnostic manner without human intervention.

# Research Questions
1. Can LLMs reason effectively without prompting?
2. To what extent can LLMs exhibit reasoning capabilities solely through decoding modifications?
3. Can decoding-based reasoning improve the confidence and reliability of LLM outputs compared to traditional greedy decoding methods?


##  Literature Review
# Key concepts and theories
1. Greedy Decoding vs. Alternative Decoding Paths
- LLMs often struggle with reasoning when following the greedy decoding path (choosing the most probable token at each step).
- Exploring alternative top-k decoding paths can reveal hidden Chain-of-Thought (CoT) reasoning, improving accuracy. 

2. Intrinsic Reasoning Capabilities of LLMs.
- The study challenges the idea that LLMs require prompts to reason effectively. 
- Instead, reasoning abilities already exist in pre-trained models but remain hidden under conventional decoding strategies.

3. CoT-Decoding Method

- A method that extracts reasoning paths by selecting decoding trajectories where the model exhibits higher confidence in the final answer. This bypasses the need for prompting and allows unsupervised reasoning extraction.

4. Model Confidence and CoT Paths

- When a CoT reasoning path is present, LLMs show greater confidence in their final answer. This confidence can be quantitatively measured to identify reliable reasoning paths.

5. Comparison with Other Methods

- Self-consistency sampling works well when CoT prompting is used but is ineffective without prompts.


## Methodology
# Data
The study uses three types of datasets to evaluate reasoning capabilities:

- Mathematical Reasoning

GSM8K: A dataset of grade-school math problems (Cobbe et al., 2021a).
MultiArith: A dataset focused on multi-step arithmetic problems (Roy & Roth, 2015).

- Commonsense Reasoning

Year Parity Task: The model is asked whether a randomly chosen celebrity was born in an even or odd year.


# Experimental Setup

The model receives a standard question-answer (QA) format.
- Decoding Strategy
Top-𝑘 Decoding:
The first decoding step considers 𝑘 = 10 alternative tokens instead of picking the most probable one (greedy decoding).
After selecting the initial token, the model continues with greedy decoding for the remaining steps.
The experiments are performed on three public models:
PaLM-2, Mistral-7B, Gemma-7B
The focus is primarily on pre-trained models, but the study also includes instruction-tuned (IT) models for comparison.


## Key Findings and Observations
# Summary of results
1. CoT-Decoding Significantly Improves Reasoning Accuracy

Across multiple language model families (PaLM-2, Mistral, and Gemma), CoT-decoding consistently enhances performance in math and commonsense reasoning tasks, often doubling or tripling accuracy compared to greedy decoding.

2. Performance Gains Across Model Scales

For PaLM-2, CoT-decoding yields +10-30% absolute accuracy gains on GSM8K.
In the year parity task, greedy decoding struggles even as model size increases, but CoT-decoding dramatically improves accuracy, nearly achieving perfect performance at larger scales.

3. Bridging the Gap Between Pre-Trained and Instruction-Tuned Models

Without any supervised data, CoT-decoding allows pre-trained models to reach accuracy levels comparable to instruction-tuned models.
It also enhances the performance of already instruction-tuned models, as they sometimes still attempt direct answering instead of following a reasoning path.

4. Impact of Top-k Choices on Accuracy

Higher values of 𝑘 (number of alternative tokens considered) improve performance, as correct reasoning paths often exist but are initially ranked lower in the decoding process.
The effect of 𝑘 is less significant in instruction-tuned models, as they naturally prioritize CoT paths.

6. CoT-Decoding vs. CoT-Prompting

CoT-decoding reveals the model’s intrinsic reasoning strategy without external human bias.
Few-shot CoT prompting, while effective, often teaches the model artificial strategies rather than uncovering its natural reasoning abilities.

7. Combining CoT-Decoding with CoT-Prompting

The combination further boosts reasoning performance across multiple models.


# Limitations
1. Model Vulnerabilities

In tasks like Coin Flip and Web of Lies, LLMs generate step-by-step CoT paths but lose track of states as complexity increases.
In multi-step arithmetic, models default to left-to-right calculations, often ignoring correct mathematical order.

2. Task Difficulty and Model Performance

Simpler tasks show stronger benefits from CoT-decoding, as correct reasoning paths are more easily identified.
As tasks become more synthetic or complex (requiring multiple reasoning steps), the model struggles to generate accurate CoT paths, indicating inherent limitations.
