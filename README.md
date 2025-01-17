# ArXiv-PDF-to-Text
#### This code can effectively convert PDF Research Papers to clean Text files, avoiding images and tables.
# Requirements
#### It requires Playwright. 
```pip install playwright```
#### It also requires firefox to be installed in Playwright environment.
```playwright install firefox```
# Compatible Softwares
#### Currently, it works only for Mozilla Firefox Browsers.
This is because of the way Firefox renders the PDFs. It does in a way quite different than other browsers. This made it advantageous and easier. 
# Features to Add
#### REMOVING PERCENTAGES, UNRECOGNIZED CHARACTERS, URLS AND KEYWORDS LIKE "CODE:", "FIGURE:", "GITHUB:" AND "WEBPAGE:"
# FAQ
#### 1. Why I did not use the ArXiv API?
<em>"This url calls the api, which returns the results in the Atom 1.0 format."</em>
To know more, click <a href="https://info.arxiv.org/help/api/basics.html">here</a> for the official documentation.
#### 2. Will additional browser support be added?
Well, I think it is easier to just install Firefox! You can open up a PDF of a research paper in other browsers vs. Firefox and understand the notable difference in the way the information is presented.
#### 3. Does it work for all OS?
Actually at the time of release it worked fine on Windows. I am not sure about other OS.
#### 4. Is there any scope for contributions?
Absolutely! If you can find a way to extract information from the unhelpful way it is displayed in other Browsers, or if you can extend support for other OS, or if you think there is a way you can further improve the quality of the extracted text, then you are welcome! Just submit a PR.
# Gratitude
#### I am grateful for the help I got from Mistral's Le Chat. It helped me overcome significant challenges.

