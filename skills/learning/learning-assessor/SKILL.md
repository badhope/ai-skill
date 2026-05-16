---
name: learning-assessor
version: 1.0.0
description: "Create learning assessments including quizzes, exams, rubrics, and evaluation criteria aligned with learning objectives. Supports multiple question types, difficulty levels, and learning analytics. Use when the user asks to create quizzes, design tests, build grading rubrics, evaluate student learning, or generate assessment questions."
author: Fullstack Skills Community
category: learning
tags: [learning-assessor]
license: MIT
platforms: [claude, cursor, gemini, codex, hermes, doubao, qwen, spark, moonshot, baidu, alibaba, bytedance]
---

----------------|-----------------------------------|-------------------------|------------------------|-----------------------|
| Code correctness  | All tests pass, handles edge cases| All tests pass          | Most tests pass        | Few tests pass        |
| Code style        | Clean, well-documented, DRY       | Readable, some comments | Inconsistent style     | Difficult to read     |
| Problem solving   | Optimal solution, explains tradeoffs| Working solution       | Partial solution       | Minimal attempt       |

**Scoring:** Total = Sum of criteria scores. A: 10-12, B: 7-9, C: 4-6, D: below 4
```

## 题目设计原则

1. **目标对齐**: 每道题目都应对应明确的学习目标
2. **难度梯度**: 覆盖不同认知层次（记忆、理解、应用、分析、评价、创造）
3. **清晰明确**: 题目表述清晰，避免歧义
4. **有效性**: 题目应能有效测量目标知识和技能

## 输出格式

- **评估目标**: 明确要评估的内容
- **评估题目**: 具体的题目、答案和解析
- **评估标准**: 详细的评分标准或 rubric
- **分析报告**: 学习分析和反馈建议

## Keywords

学习评估, 测验设计, 评分标准, rubric, 考试题目, quiz, test, exam, grading, assessment, evaluation
