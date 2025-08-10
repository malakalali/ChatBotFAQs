from matcher import FAQMatcher, get_best_match

def test_question_matching():
    print("Testing FAQ Question Matching System")
    print("=" * 50)
    
    # Initialize matcher
    matcher = FAQMatcher()
    
    # Test cases with expected matches
    test_cases = [
        {
            "question": "I forgot my password, how do I reset it?",
            "expected_keywords": ["reset", "password"],
            "description": "Password reset question"
        },
        {
            "question": "What time are you open?",
            "expected_keywords": ["business", "hour"],
            "description": "Business hours question"
        },
        {
            "question": "Where is my order?",
            "expected_keywords": ["track", "order"],
            "description": "Order tracking question"
        },
        {
            "question": "Can I return this item?",
            "expected_keywords": ["return", "policy"],
            "description": "Return policy question"
        },
        {
            "question": "Do you deliver to other countries?",
            "expected_keywords": ["ship", "internationally"],
            "description": "International shipping question"
        },
        {
            "question": "How do I contact customer service?",
            "expected_keywords": ["contact", "customer", "support"],
            "description": "Customer support contact question"
        },
        {
            "question": "What credit cards do you accept?",
            "expected_keywords": ["payment", "method"],
            "description": "Payment methods question"
        },
        {
            "question": "How long will shipping take?",
            "expected_keywords": ["shipping", "take"],
            "description": "Shipping time question"
        },
        {
            "question": "I want to cancel my order",
            "expected_keywords": ["cancel", "order"],
            "description": "Order cancellation question"
        },
        {
            "question": "Do you give discounts for large orders?",
            "expected_keywords": ["discount", "bulk", "order"],
            "description": "Bulk order discounts question"
        }
    ]
    
    print("\nTesting Individual Questions:")
    print("-" * 50)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\nTest {i}: {test_case['description']}")
        print(f"Question: '{test_case['question']}'")
        
        # Get best match
        match = matcher.get_best_match(test_case['question'])
        
        if match:
            print(f"✓ Matched: '{match['question']}'")
            print(f"  Similarity Score: {match['similarity_score']:.3f}")
            print(f"  Answer: {match['answer'][:80]}...")
        else:
            print("✗ No match found")
    
    print("\n" + "=" * 60)
    print("Testing Top Matches Functionality:")
    print("-" * 50)
    
    # Test ambiguous question
    ambiguous_question = "What about my order?"
    print(f"\nAmbiguous Question: '{ambiguous_question}'")
    print("Top 3 matches:")
    
    top_matches = matcher.get_top_matches(ambiguous_question, top_k=3)
    for i, match in enumerate(top_matches, 1):
        print(f"  {i}. '{match['question']}' (Score: {match['similarity_score']:.3f})")
    
    print("\n" + "=" * 60)
    print("Testing Direct Answer Function:")
    print("-" * 50)
    
    # Test direct answer function
    test_questions = [
        "How do I reset my password?",
        "What are your hours?",
        "Can I get my money back?",
        "Do you ship to Canada?"
    ]
    
    for question in test_questions:
        answer = matcher.get_answer(question)
        print(f"\nQ: {question}")
        print(f"A: {answer}")
    
    print("\n" + "=" * 60)
    print("Testing Edge Cases:")
    print("-" * 50)
    
    # Test edge cases
    edge_cases = [
        "",  # Empty string
        "   ",  # Whitespace only
        "xyz123",  # No meaningful words
        "This is a very long question that doesn't match any of our FAQs and should return no results"
    ]
    
    for case in edge_cases:
        result = matcher.get_best_match(case)
        print(f"\nInput: '{case}'")
        if result:
            print(f"Result: '{result['question']}' (Score: {result['similarity_score']:.3f})")
        else:
            print("Result: No match found")

def test_similarity_thresholds():
    print("\n" + "=" * 60)
    print("Testing Similarity Thresholds:")
    print("-" * 50)
    
    matcher = FAQMatcher()
    test_question = "How do I reset my password?"
    
    thresholds = [0.05, 0.1, 0.2, 0.3, 0.5]
    
    for threshold in thresholds:
        match = matcher.get_best_match(test_question, threshold=threshold)
        if match:
            print(f"Threshold {threshold}: ✓ Match found (Score: {match['similarity_score']:.3f})")
        else:
            print(f"Threshold {threshold}: ✗ No match found")

if __name__ == "__main__":
    test_question_matching()
    test_similarity_thresholds()
