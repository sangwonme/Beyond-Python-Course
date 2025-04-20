# Prompting Techniques


## Zero-Shot Prompting
- **Zero-Shot**: 별도의 예시 없이 지시만 주고 문제를 바로 해결하게 하는 방식.
- 모델이 학습된 일반 지식을 바탕으로 답변.

#### 예시
```
Translate this sentence into English: 나는 학교에 갑니다.
```

**사용할 때**: 문제가 간단하거나 명확할 때.


## One-Shot Prompting
- **One-Shot**: 예시 하나를 주고 비슷한 문제를 풀게 하는 방식.

#### 예시
```
Input: 나는 집에 간다. → I go home.
Input: 나는 학교에 간다. →
```

**사용할 때**: 아웃풋이 따라할 규칙이 있으며, 단일한 예시로도 충분히 규칙을 유추할 수 있을 때.


## Few-Shot Prompting
- **Few-Shot**: 예시를 여러 개 주어, 모델이 패턴을 학습한 뒤 문제를 해결하게 하는 방식.

#### 예시
```
Input: 나는 집에 간다. → I go home.
Input: 그는 밥을 먹는다. → He eats food.
Input: 우리는 영화를 본다. → We watch a movie.
Input: 너는 학교에 간다. →
```

**사용할 때**: 패턴이나 스타일을 명확히 학습시킬 필요가 있을 때.
- 단순한 문제 해결뿐 아니라, 패턴 인식과 일반화 능력을 유도할 수 있다.
- 다양한 예시를 통해 모델의 일관성 있는 응답을 이끌어낸다.


## Chain-of-Thought (CoT) Prompting
- **Chain-of-Thought**: 모델이 생각 과정을 단계별로 서술하도록 유도하여 복잡한 문제를 해결하는 방식.

#### 예시
```
Q: I bought 3 apples and 2 bananas. Apples cost 1000 won each, and bananas cost 500 won each. What is the total cost?
A: 3 apples cost 3000 won. 2 bananas cost 1000 won. So the total is 4000 won.

Q: I bought 4 apples and 1 pineapple. Apples cost 2500 won each, and pineapple cost 1000 won each. What is the total cost?
A: 
```

**사용할 때**: 문제가 복잡해 오답을 내기 쉬운 상황에서, 중간 추론 단계를 명시해 복잡한 문제를 더 정확히 풀 수 있게 돕는다.


## Self-Consistency Prompting
- **Self-Consistency**: Chain-of-Thought를 여러 번 수행하여 다양한 경로로 답을 유도한 뒤, 가장 자주 등장하는 답을 최종 정답으로 선택하는 방식.

#### 예시
```
Q: 237 + 468은 얼마인가?
(Chain-of-Thought로 5번 답변 생성) → 가장 많이 등장한 답 705를 최종 답으로 채택.
```

**사용할 때**: 정확도가 요구될 때, 불안정한 추론을 보완하고 정답 신뢰도를 높이기 위해 사용한다.
