import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px







st.write('''<br><br><br><center><font color = "#0000ff" size = 7>PENELUSURAN LITERATUR GENERALIZED LAMBDA DISTRIBUTION (GLD)</font></center>



             ''', unsafe_allow_html = True)

















st.write('''<style>
         a:hover {
         background-color: yellow;
         text-decoration: none;
         }
         </style>''', unsafe_allow_html=True)





pilih_topik = st.radio(
    "Tahun Terbit Artikel: ",
    [":rainbow[1955]",":rainbow[1978]", ":rainbow[1979]" ,  ":rainbow[1986]", ":rainbow[1988]"  ,":rainbow[1991]",":rainbow[1993]",":rainbow[1999]",":rainbow[2000]",":rainbow[2001]", ":rainbow[2007]", ":rainbow[2008]", ":rainbow[2009]", ":rainbow[2010]",":rainbow[2011]",  ":rainbow[2015]",":rainbow[Buku Optimisasi]",     ])






if pilih_topik == ":rainbow[1955]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1955</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: A Million Random Digits with 100,000 Normal Deviates</font><br><font color = "#ff00ff">Jurnal: </font><br><font color = "#f4c430">Tahun Terbit Artikel: 1955</font><br><font color = "#32cd32">Publisher: RAND</font><br><a href = "https://www.amazon.com/Million-Random-Digits-Normal-Deviates/dp/0833030477" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.amazon.com/Million-Random-Digits-Normal-Deviates/dp/0833030477">
    <img src="https://statkomat.com/GLD/1955/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)











if pilih_topik == ":rainbow[1978]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1978</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: A new measure of irregularity of distribution</font><br><font color = "#ff00ff">Jurnal: Bulletin of the American Mathematical Society</font><br><font color = "#f4c430">Tahun Terbit Artikel: 1978</font><br><font color = "#32cd32">Publisher: American Mathematical Society</font><br><a href = "https://www.ams.org/journals/bull/1978-84-06/S0002-9904-1978-14532-7/" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.ams.org/journals/bull/1978-84-06/S0002-9904-1978-14532-7/">
    <img src="https://statkomat.com/GLD/1978/1/1.png" width="800"><br>
    <img src="https://statkomat.com/GLD/1978/1/2.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)













if pilih_topik == ":rainbow[1979]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1979</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Fitting a distribution to data using an alternative to moments</font><br><font color = "#ff00ff">Jurnal: IEEE Proceedings of the 1979 Winter Simulation Conference</font><br><font color = "#f4c430">Tahun Terbit Artikel: 1979</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://dl.acm.org/doi/10.5555/800134.804366" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://dl.acm.org/doi/10.5555/800134.804366">
    <img src="https://statkomat.com/GLD/1979/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)

























if pilih_topik == ":rainbow[1986]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1986</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Goodness-of-Fit Techniques</font><br><font color = "#ff00ff">Jurnal: </font><br><font color = "#f4c430">Tahun Terbit Artikel: 1986</font><br><font color = "#32cd32">Publisher: Taylor & Francis</font><br><a href = "https://www.taylorfrancis.com/books/edit/10.1201/9780203753064/goodness-fit-techniques-ralphb-agostino" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.taylorfrancis.com/books/edit/10.1201/9780203753064/goodness-fit-techniques-ralphb-agostino">
    <img src="https://statkomat.com/GLD/1986/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)











if pilih_topik == ":rainbow[1988]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1988</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: a study of the generalized tukey lambda family</font><br><font color = "#ff00ff">Jurnal: Communications in Statistics - Theory and Methods</font><br><font color = "#f4c430">Tahun Terbit Artikel: 1988</font><br><font color = "#32cd32">Publisher: Taylor & Francis</font><br><a href = "https://www.tandfonline.com/doi/abs/10.1080/03610928808829820" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.tandfonline.com/doi/abs/10.1080/03610928808829820">
    <img src="https://statkomat.com/GLD/1988/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)




















if pilih_topik == ":rainbow[1991]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1991</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: A new measure of irregularity of distribution</font><br><font color = "#ff00ff">Jurnal: Journal of Number Theory</font><br><font color = "#f4c430">Tahun Terbit Artikel: 1991</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/pii/0022314X9190055G" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/pii/0022314X9190055G">
    <img src="https://statkomat.com/GLD/1991/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)













if pilih_topik == ":rainbow[1993]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1993</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Random and quasirandom sequences: Numerical estimates of uniformity of distribution</font><br><font color = "#ff00ff">Jurnal: Mathematical and Computer Modelling</font><br><font color = "#f4c430">Tahun Terbit Artikel: 1993</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/pii/089571779390160Z" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/pii/089571779390160Z">
    <img src="https://statkomat.com/GLD/1993/1/2.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)














if pilih_topik == ":rainbow[1999]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 1999</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Theory & Methods: A Starship Estimation Method for the Generalized Lambda Distributions</font><br><font color = "#ff00ff">Jurnal: Australian & New Zealand Journal of Statistics</font><br><font color = "#f4c430">Tahun Terbit Artikel: 1999</font><br><font color = "#32cd32">Publisher: Wiley</font><br><a href = "https://onlinelibrary.wiley.com/doi/10.1111/1467-842X.00089" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://onlinelibrary.wiley.com/doi/10.1111/1467-842X.00089">
    <img src="https://statkomat.com/GLD/1999/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)


























if pilih_topik == ":rainbow[2000]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 2000</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Estimating the Parameters of the Generalized Lambda Distribution</font><br><font color = "#ff00ff">Jurnal: ALGO RESEARCH QUARTERLY</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2000</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://www.researchgate.net/requests/r124245353" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.researchgate.net/requests/r124245353">
    <img src="https://statkomat.com/GLD/2000/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)






if pilih_topik == ":rainbow[2001]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 2001</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Option Pricing Based on the Generalized Lambda Distribution</font><br><font color = "#ff00ff">Jurnal: The Journal of Futures Markets</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2001</font><br><font color = "#32cd32">Publisher: John Wiley & Sons, Inc</font><br><a href = "https://onlinelibrary.wiley.com/doi/10.1002/1096-9934(200103)21:3%3C213::AID-FUT2%3E3.0.CO;2-H" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://onlinelibrary.wiley.com/doi/10.1002/1096-9934(200103)21:3%3C213::AID-FUT2%3E3.0.CO;2-H">
    <img src="https://statkomat.com/GLD/2001/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)











if pilih_topik == ":rainbow[2007]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 2007</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: L-moments and TL-moments of the generalized lambda distribution</font><br><font color = "#ff00ff">Jurnal: Computational Statistics & Data Analysis</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2007</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/abs/pii/S0167947306002301" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/abs/pii/S0167947306002301">
    <img src="https://statkomat.com/GLD/2007/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)



    st.write('''<br><br><br>[2] <font color = "#0000ff">Judul: Numerical maximum log likelihood estimation for generalized lambda distributions</font><br><font color = "#ff00ff">Jurnal: Computational Statistics & Data Analysis</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2007</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/abs/pii/S0167947306001988" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/abs/pii/S0167947306001988">
    <img src="https://statkomat.com/GLD/2007/2/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)





    st.write('''<br><br><br>[3] <font color = "#0000ff">Judul: Estimating the parameters of a generalized lambda distribution</font><br><font color = "#ff00ff">Jurnal: Computational Statistics & Data Analysis</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2007</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/abs/pii/S0167947306003677" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/abs/pii/S0167947306003677">
    <img src="https://statkomat.com/GLD/2007/3/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)

















if pilih_topik == ":rainbow[2008]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 2008</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Characterizing the generalized lambda distribution by L-moments</font><br><font color = "#ff00ff">Jurnal: Computational Statistics & Data Analysis</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2007</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/abs/pii/S016794730700254X" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/abs/pii/S016794730700254X">
    <img src="https://statkomat.com/GLD/2008/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)
























if pilih_topik == ":rainbow[2009]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 2009</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Confidence intervals for quantiles using generalized lambda distributions</font><br><font color = "#ff00ff">Jurnal: Computational Statistics & Data Analysis</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2009</font><br><font color = "#32cd32">Publisher: Elsevier</font><br><a href = "https://www.sciencedirect.com/science/article/abs/pii/S0167947309000437" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.sciencedirect.com/science/article/abs/pii/S0167947309000437">
    <img src="https://statkomat.com/GLD/2009/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)





    st.write('''[2]<br><br><br <font color = "#0000ff">Judul: The Generalized Lambda Distribution as an Alternative to Model Financial Returns</font><br><font color = "#ff00ff">Jurnal: ETH Econohysics Working and White Papers Series</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2009</font><br><font color = "#32cd32">Publisher: </font><br><a href = "https://www.rmetrics.org/sites/default/files/2009-01-glambdaDist.pdf" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.rmetrics.org/sites/default/files/2009-01-glambdaDist.pdf">
    <img src="https://statkomat.com/GLD/2009/2/1.png" width="800"><br>
    <img src="https://statkomat.com/GLD/2009/2/2.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)





















































if pilih_topik == ":rainbow[2011]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 2011</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Handbook of Fitting Statistical Distributions with R</font><br><font color = "#ff00ff">Jurnal: </font><br><font color = "#f4c430">Tahun Terbit Artikel: 2011</font><br><font color = "#32cd32">Publisher: Taylor and Francis Group</font><br><a href = "https://www.taylorfrancis.com/books/mono/10.1201/b10159/handbook-fitting-statistical-distributions-zaven-karian-edward-dudewicz" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.taylorfrancis.com/books/mono/10.1201/b10159/handbook-fitting-statistical-distributions-zaven-karian-edward-dudewicz">
    <img src="https://statkomat.com/GLD/2011/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)

















if pilih_topik == ":rainbow[2015]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Artikel Tahun Terbit 2015</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <font color = "#0000ff">Judul: Estimating the Parameters of the Generalized Lambda Distribution: Which Method Performs Best?</font><br><font color = "#ff00ff">Jurnal: Communications in Statistics - Simulation and Computation</font><br><font color = "#f4c430">Tahun Terbit Artikel: 2015</font><br><font color = "#32cd32">Publisher: Taylor & Francis</font><br><a href = "https://www.tandfonline.com/doi/full/10.1080/03610918.2014.901355?scroll=top&needAccess=true" target = "_blank" style = "text-decoration:none">Link Artikel</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://www.tandfonline.com/doi/full/10.1080/03610918.2014.901355?scroll=top&needAccess=true">
    <img src="https://statkomat.com/GLD/2015/1/1.png" width="800"><br>
    </a>""",
    unsafe_allow_html=True)













if pilih_topik == ":rainbow[Buku Optimisasi]":
    st.write('''<br><br><br><center><font color = "red" size = 7>Daftar Buku Optimisasi</font></center> ''', unsafe_allow_html = True)

    st.write('''[1] <br><a href = "https://drive.google.com/drive/folders/1QRfF5JxMJoZ4ApuPxb4x5WMPbo6Cr1I2?usp=sharing" target = "_blank" style = "text-decoration:none">Link Buku</a>



             ''', unsafe_allow_html = True)
    

    st.markdown(
    """<a href="https://drive.google.com/drive/folders/1QRfF5JxMJoZ4ApuPxb4x5WMPbo6Cr1I2?usp=sharing">
    <img src="https://statkomat.com/GLD/Buku Optimisasi/1.png" width="500"><br>
    </a>""",
    unsafe_allow_html=True)


















st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")




st.markdown(
    """<center><img src="https://statkomat.com/gambar/ugi.png" width="500"></center>
    <h2 style='text-align: justify; color: blue;'><center>Prana Ugiana Gio, Founder of <a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'><font color = 'orange'>STATCAL</a></center></h2>""",
    unsafe_allow_html=True)




col1, col2, col3, col4, col5, col6 = st.columns([2, 2, 2, 2, 2, 2])
with col1:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/logo_figshare2.png" width="50"><br><a href = 'https://figshare.com/authors/prana_ugiana_gio/17826386' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>FIGSHARE</b></font></center></a>""",unsafe_allow_html=True)
with col2:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statkomat.gif" width="50"><br><a href = 'https://statkomat.com/download_tulisan.php' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATKOMAT</b></font></center></a>""",unsafe_allow_html=True)
with col3:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/youtube.png" width="50"><br><a href = 'https://www.youtube.com/@STATKOMAT/videos' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>YOUTUBE</b></font></center></a>""",unsafe_allow_html=True)
with col4:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/literature-review.gif" width="50"><br><a href = 'https://literaturereview.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LITERATURE REVIEW</b></font></center></a>""",unsafe_allow_html=True)
with col5:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/list-papers.gif" width="50"><br><a href = 'https://daftar-paper.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>LIST OF JOURNALS</b></font></center></a>""",unsafe_allow_html=True)
with col6:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/my-papers.gif" width="50"><br><a href = 'https://ugi-publikasi.streamlit.app/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>MY PAPERS</b></font></center></a>""",unsafe_allow_html=True)

st.markdown("")
st.markdown("")

col7, col8, col9, col10, col11, col12 = st.columns([2, 2, 2, 2, 2, 2])
with col7:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/pls-sem.gif" width="50"><br><a href = 'https://aplikasi-plssem.streamlit.app//' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STRUCTURAL EQUATION MODELING (PLS-SEM)</b></font></center></a>""",unsafe_allow_html=True)
with col8:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/statcal.gif" width="50"><br><a href = 'https://statcal.com/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>STATCAL</b></font></center></a>""",unsafe_allow_html=True)
with col9:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/shiny.gif" width="50"><br><a href = 'https://share-your-shiny-app.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>SHINY</b></font></center></a>""",unsafe_allow_html=True)
with col10:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/ugi-gio.gif" width="50"><br><a href = 'https://ugi-gio.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>UGI</b></font></center></a>""",unsafe_allow_html=True)
with col11:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/indcomp.gif" width="50"><br><a href = 'https://indcomp-stats.id/' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>INDCOMP</b></font></center></a>""",unsafe_allow_html=True)
with col12:
    st.markdown("""<center><img src="https://statkomat.com/streamlit-ugi/github.png" width="50"><br><a href = 'https://github.com/gioprana89' target = '_blank' style = 'text-decoration:none'></center><center><font color = 'orange'><b>GITHUB</b></font></center></a>""",unsafe_allow_html=True)







st.markdown("")
st.markdown("")

st.markdown("""<a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><center><img src="https://statkomat.com/streamlit-ugi/kopi.gif" width="150"></center></a><br><center><b><a href = 'https://saweria.co/statkomat' target = '_blank' style = 'text-decoration:none'><font color = 'orange' size = 7>Buy Me a Cup of Coffee</font></a></b></font></center>""",unsafe_allow_html=True)
