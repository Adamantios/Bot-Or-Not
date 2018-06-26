# Bot-Or-Not
A project using a model or a combination of models, in order to be trained to predict if a twitter user is a Bot or not. Written in Python 2.7

## Input
Bot Or Not takes as an input a folder which contains the twitter users data in json format,  
created from [Twitter Profile Parser](https://github.com/Adamantios/Twitter-Profile-Parser/blob/master/README.md)
with an extra field `is_bot` which is either True or False.

## Requirements
numpy  
scikit_learn

## Usage
```
bot_or_not.py [-h] -i IN_FOLDER [-n NUM_FOLDS]

optional arguments:
  -h, --help            show this help message and exit
  
  -i IN_FOLDER, --input IN_FOLDER
                        path to folder with pan dataset for a language
                        
  -n NUM_FOLDS, --numfolds NUM_FOLDS
                        Number of folds to use in cross validation
```
## Results
A result.txt file is being created, containing statistics and information about the results of the model.  
The results are also being printed in the console.

## Example results for 1000 users - 500 bots and 500 non bots.
```
------------- Created at: 20/09/2016 10:55:59 -------------
Loading dataset...
Loaded 1000 users...
Creating model for Bot detection...

---------------- Performing Grid Search CV ----------------
Parameters: {}
Training instances: 1000
Using 4 fold validation.
Preprocessing...
Fitting...

------------------------- Results -------------------------
Results for Bot detection with estimator:
 [('features', FeatureUnion(n_jobs=1,
       transformer_list=[('soac_model', SOACModel(max_df=1.0, max_features=None, min_df=1, threshold=0.1))],
       transformer_weights=None)), ('svm', LinearSVC(C=0.1, class_weight='balanced', dual=True, fit_intercept=True,
     intercept_scaling=1, loss='squared_hinge', max_iter=1000,
     multi_class='ovr', penalty='l2', random_state=None, tol=0.0001,
     verbose=0))]
Grid Scores: [mean: 0.86300, std: 0.02161, params: {}]
Runtime: 8.21899986267 seconds.
```

## Future Enhancement
Pass two different lists of twitter users. One to train the model and one to predict if its users are bots or not.
