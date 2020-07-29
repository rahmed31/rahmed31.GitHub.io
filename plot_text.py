from bokeh.models import Div

#header
header = Div(text="""<h1>MHD LITERATURE CLUSTERING</h1>""")

# project description
description = Div(text="""<p1>From approximately 1960-1990 the DOE funded a massive research program into magnetohydrodynamic (MHD) power generation. The MHD group has recently digitized a collection of yearly conference proceedings that took place during this period, the Symposium on the Engineering Aspects of Magnetohydrodynamics (SEAMs). The purpose of this study is to apply Python-based natural language processing (NLP) and machine-learning (ML) algorithms to this large body of literature, so as to discover connections between topics and subfields that could provide useful insights to current MHD power research efforts.</p1>
<br><br>
<p1> The developed code begins with conducting optical character recognition on the scanned PDF files to produce text data which is subsequently cleaned with a custom-built text processer. TF-IDF vectorization is used to create a vector representation of each document, which is weighted according to the importance of each word in the corpus as a whole. As a first application, we are able to represent an input text of interest in this vector space to determine the most similar articles. We also apply NLP and ML algorithms to study the SEAMs collection itself. SEAMs documents are clustered using an unsupervised machine-learning k-means approach, and the topics describing each cluster are found using latent Dirichlet allocation topic modeling. The combination of these two provide a powerful computational method for document categorization and discovering relations between papers from different time periods and different human-assigned topical areas.  Finally, we developed this interactive visualization tool to facilitate researchers in exploring these relationships, as well as finding papers of interest. </p1>""")

# steps description
description2 = Div(text="""<h3>The Approach in Depth:</h3>
<ul>
  <li>Use PDFBox to split each PDF into individual documents using page indices. Organize each scanned collection of SEAMs by Edition and Session. </li>
  <li>Run Optical Character Recognition (OCR) on each scanned document using the open-source Tesseract OCR Engine. </li>
  <li>Parse the text from the body of each document using the PyPDF2 package. </li>
  <li>Process the corpus using a custom-made MHD text pre-processing pipeline. </li>
  <li>Turn each document instance di into a feature vector Xi using Term Frequency-Inverse Document Frequency (TF-IDF).</li>
  <li>Using the fitted TF-IDF vectorization model, find similar texts using vector space cosine similarity.</li>
  <li>Apply Dimensionality Reduction to each feature vector Xi using t-Distributed Stochastic Neighbor Embedding (t-SNE) to cluster similar research articles in the two dimensional plane X embedding Y1.</li>
  <li>Use Principal Component Analysis (PCA) to project down the dimensions of X to a number of dimensions that will keep .95 variance while removing noise and outliers in embedding Y2.</li>
  <li>Apply k-means clustering on Y2 to label each cluster on Y1.</li>
  <li>Apply Topic Modeling on X using Latent Dirichlet Allocation (LDA) to discover topic words from each cluster.</li>
  <li>Investigate the clusters visually on the plot, zooming down to specific articles as needed, and via classification using Stochastic Gradient Descent (SGD).</li>
</ul>
""")

description_search = Div(text="""<h3>Filter by Text:</h3><p1>Search keyword to filter out the plot. It will search pre-processed texts,
titles, and authors. Press enter when ready.
Clear and press enter to reset the plot.</p1>""")

description_slider = Div(text="""<h3>Filter by the Clusters:</h3><p1>The slider below can be used to filter the target cluster.
Adjust the slider to the desired cluster number to display the plots that belong to that cluster.
Slide back to the right to show all.</p1>""")

description_text_input = Div(text="""<h3>Find Similar Research Papers:</h3><p1>Input a TXT or PDF file of interest to
the find the top 10 most similar research papers from the SEAMs collection.
The output will be saved in the current working directory of the input file as "TextRecommendations[i].csv" and will automatically launch for viewing.</p1>""")

description_keyword = Div(text="""<h3>Keywords:</h3>""")

description_current = Div(text="""<h3>Selected:</h3>""")

# citation
cite = Div(text="""<p1><h3>Citations:</h3>
<p1>Eren, M. E., Solovyev, N., Nicholas, C., &amp; Raff, E. (2020, April). COVID-19 Literature Clustering [Scholarly project]. In COVID-19 Literature Clustering. Retrieved May 23, 2020, from <a href="https://github.com/MaksimEkin/COVID19-Literature-Clustering">https://github.com/MaksimEkin/COVID19-Literature-Clustering</a> </p1>
<br><br>
<p1>Lavin, M. J. (2019). Analyzing Documents with TF-IDF. Programming Historian, 8. doi:10.46430/phen0082</p1>
<br><br>
<p1>Jackson, D. (1993). Stopping Rules in Principal Components Analysis: A Comparison of Heuristical and Statistical Approaches. Ecology, 74(8), 2204-2214. doi:10.2307/1939574</p1>
<br><br>
<p1>Maaten, L. V., &amp; Hinton, G. (2008). Visualizing Data using t-SNE. Journal of Machine Learning Research, 9, 2579-2605.</p1>""")


notes = Div(text="""<h3>Contact:</h3><p1>Northeastern Illinois University (NEIU) <br>
                                <b>Project Author: </b>Raihan Ahmed (rahmed10@neiu.edu)<br>
                                <b>LinkedIn: </b><a href="https://www.linkedin.com/in/raihan-ahmed1">https://www.linkedin.com/in/raihan-ahmed1</a><br>
                                <b>PI: </b>Dr. Lee Aspitarte<br>
                                <b>GitHub: </b><a href="https://github.com/rahmed31/RA_NLP_MHD">https://github.com/rahmed31/RA_NLP_MHD</a>
                                <br><br><b>Many thanks to</b> the scientific and software development community
<b>for their open source contributions and collective problem solving.</b> </p1>
<br>
<h3>Latest Update(s):</h3><p1> The GitHub repository not yet public. Active developments are being made to improve code, visualization efforts, and repository organization. </p1>""")

dataset_description = Div(text="""<h3>Dataset Description:</h3><p1>The corpus used in this project consists of an OCRed collection of SEAMs ranging from the 3rd (1962) edition through the 34th edition (1997). Each collection of SEAMs is composed of a number of different sessions (usually around 12) labeled by a common topic (i.e. Systems and Optimization, or Plasma and Flow Phenomena) by the papers featured in it. Keep in mind, these texts were never digitized prior to their publication. Each collection of scanned PDFs vary in shade or quality, thereby allowing for sizeable error in natural language to machine language translation. The texts were processed and corrected using the best available methods to circumvent this issue.</i>

<p>Total of <b>1,513 samples (about 18,000 pages)</b> analyzed.</p1>""")
