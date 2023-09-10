from question import Question
questionPrompts=[
    "What color are apples?\n(a)Red/Green\n(b)Purple\n(c)Orange\n\n",
    "What color are bananas?\n(a)Teal\n(b)Magenta\n(c)Yellow\n\n",
    "What color are Strawberries?\n(a)yellow\n(b)Red\n(c)Blue\n\n"
]
#
questions=[
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "b")
]







def runTest(question):
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
            score+=1
    print("You got ",score,"/",len(questions)," correct")

runTest(questions)