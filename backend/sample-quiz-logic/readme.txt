Prototyping some python logic for the  quiz questions.

Requirements of the quiz:
1) Should be able to access quiz data from csv's. User chooses which categs 
	they wish to 'generate' questions from eg. sport, music etc.

2) Randomly sample questions without replacement (prevent repeat q's).
	User would specify some num of questions they wish to have.
	User requested questions should be constant across all categories.

3) Store these questions and their relevant answers in data structure.
	If question is multi-choice we should also select incorrect answers
		and store these as well in the structure.

4) Serve a question to the user with possible answers. Keep track of question
	already served.	 

5) Record users answer to question. Provide feedback if correct/incorrect.
	If correct: increment their quiz total score.
	5.1) Also tracking quiz stats to display either after each q or at 
		end of quiz.
	Over-time we need to track the number of user selections  each possible
		question answer has had. 
	We then generate a graph of this data and serve to user. 
