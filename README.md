# Bot-Or-Not
A model, which predicts if a twitter user is a Bot or not. Written in Python 2.7

##Input
Bot Or Not takes as an input a folder which contains the twitter user's data in json format.

##Requirements
numpy  
scikit_learn

##Usage
```
bot_or_not.py [-h] -i IN_FOLDER [-n NUM_FOLDS]

optional arguments:
  -h, --help            show this help message and exit
  
  -i IN_FOLDER, --input IN_FOLDER
                        path to folder with pan dataset for a language
                        
  -n NUM_FOLDS, --numfolds NUM_FOLDS
                        Number of folds to use in cross validation
```
##Results
A result.txt file is being created, containing statistics and information about the results of the model.  
The results are also being printed in the console.

##Example results for 1000 users. 500 bots and 500 non bots.
```

```
