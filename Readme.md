Final Project Advanced Programming in R
======

 explantion about the diffrent files:
 
- **code.Rmd** - the R code to implemnt all the plots, classifcation and refression models and all the statitical parmeters in the papers.
- **code.html** - same code as the **code.Rmd** just knite.
- **pre_process.py** - the implemtation to pre-process the data from  the PeerReview paper[ github reposetory](https://github.com/allenai/PeerRead) note: you can change the columns you want from the dataset in the **json_keys** parmeter in the function set_data.
- **peer_read_bert.ipynb** - the noteook that implemnt the semi superviesd teacher-studet fine tune bert that predict the recomndation score from the reviwer comment. 
- **Data** -  Directory that has two csv files:
	1. **data.csv** - the csv that the **pre_process.py** code return 	from the  PeerReview paper data(19000 rows).
	2. **clean_data.csv** - only the rows that have all the feachers 		we 		train on(308 rows)
- **requirments.txt** - list of all the requirments libraries to run the **peer_read_bert.ipynb** notbook on your enviorment.
- **Readme.md** - this file :blush:

Instructions for replicating our analysis of the project
------
For implemnt the R code:

  1.Make a new directory in the directory where the 		code.Rmd file is located and name it Data.
  
  2.Insert clean_data.csv into the new Data directory.</li>

For implemnt the ipynb code:

	
1. Make sure that you have in your enviorment all the libraries in 	requirments.txt.
  
2. login to your weights and bisas user in section **login and 		setting weights and bisas**, if you dont want to use weights 		and bisas notice that you would need to change the train 		function for the model 
3. change the path in the line
```
df = pd.read_csv("/content/data.csv")
``` 
 to the path of **data.csv**.

spacial thanks to :

- [huggingface:hugs:](https://huggingface.co)
- [PeerReview](https://github.com/allenai/PeerRead) 
- [PapersWithCode](https://paperswithcode.com)

And of course my parter for the work **Snir Aharon Ezer**.



