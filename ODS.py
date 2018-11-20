
import telebot
from telebot import apihelper

bot = telebot.TeleBot("TOKEN HERE")
apihelper.proxy = {
  'https': 'socks5://telegram:telegram@wmwdt.tgvpnproxy.me:1080'
}


def getArticles():
  """
  return tuple of tuples
  """
  return ((11, 'Large scale study of anti-sense regulation by differential network analysis', 'https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0613-7', 'BMC Systems Biology', datetime.date(2018, 11, 20), 'Authors: Marc Legeay, Sébastien Aubourg, Jean-P
ierre Renou and Béatrice Duval', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2018, 11, 20, 13, 56, 45)), (12, 'On the reconstruction of the ancestral bacterial genomes in genus Mycobacterium and Brucella', 'https://bmcsystbiol.biomedcentra
l.com/articles/10.1186/s12918-018-0618-2', 'BMC Systems Biology', datetime.date(2018, 11, 20), 'Authors: Christophe Guyeux, Bashar Al-Nuaimi, Bassam AlKindy, Jean-François Couchot and Michel Salomon', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.dat
etime(2018, 11, 20, 13, 56, 45)), (13, 'Pipeline design to identify key features and classify the chemotherapy response on lung cancer patients using large-scale genetic data', 'https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0615-5', 'BMC Sys
tems Biology', datetime.date(2018, 11, 20), 'Authors: María Gabriela Valdés, Iván Galván-Femenía, Vicent Ribas Ripoll, Xavier Duran, Jun Yokota, Ricard Gavaldà, Xavier Rafael-Palou and Rafael de Cid', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.dat
etime(2018, 11, 20, 13, 56, 45)), (14, 'BLASSO: integration of biological knowledge into a regularized linear model', 'https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0612-8', 'BMC Systems Biology', datetime.date(2018, 11, 20), 'Authors: Danie
l Urda, Francisco Aragón, Rocío Bautista, Leonardo Franco, Francisco J. Veredas, Manuel Gonzalo Claros and José Manuel Jerez', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2018, 11, 20, 13, 56, 45)), (15, 'SWIFOLD: Smith-Waterman implementa
tion on FPGA with OpenCL for long DNA sequences', 'https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0614-6', 'BMC Systems Biology', datetime.date(2018, 11, 20), 'Authors: Enzo Rucci, Carlos Garcia, Guillermo Botella, Armando De Giusti, Marcelo
Naiouf and Manuel Prieto-Matias', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2018, 11, 20, 13, 56, 45)), (16, 'Improving the EFMs quality by augmenting their representativeness in LP methods', 'https://bmcsystbiol.biomedcentral.com/articl
es/10.1186/s12918-018-0619-1', 'BMC Systems Biology', datetime.date(2018, 11, 20), 'Authors: José F. Hidalgo, Jose A. Egea, Francisco Guil and José M. García', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2018, 11, 20, 13, 56, 45)), (17, 'A
dvanced integration of fluid dynamics and photosynthetic reaction kinetics for microalgae culture systems', 'https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0611-9', 'BMC Systems Biology', datetime.date(2018, 11, 20), 'Authors: Stepan Papacek,
 Jiri Jablonsky and Karel Petera', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2018, 11, 20, 13, 56, 45)), (18, 'BioGraph: a web application and a graph database for querying and analyzing bioinformatics resources', 'https://bmcsystbiol.bi
omedcentral.com/articles/10.1186/s12918-018-0616-4', 'BMC Systems Biology', datetime.date(2018, 11, 20), 'Authors: Antonio Messina, Antonino Fiannaca, Laura La Paglia, Massimo La Rosa and Alfonso Urso', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.d
atetime(2018, 11, 20, 13, 56, 45)), (19, 'Ultraviolet (IUV) and mass spectrometry (IMS) imaging for the deconvolution of microbial interactions', 'https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0617-3', 'BMC Systems Biology', datetime.date(20
18, 11, 20), 'Authors: Víctor González-Menéndez, Germán Martínez, Rachel Serrano, Francisca Muñoz, Jesús Martín, Olga Genilloud and José R. Tormo', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2018, 11, 20, 13, 56, 45)), (20, 'Historical bi
ogeography reveals new independent evolutionary lineages in the Pantosteus plebeius-nebuliferus species-group (Actinopterygii: Catostomidae)', 'https://bmcevolbiol.biomedcentral.com/articles/10.1186/s12862-018-1286-y', 'BMC Evolutionary Biology', datetime.date(
2018, 11, 20), 'Authors: Diushi Keri Corona-Santiago, Omar Domínguez-Domínguez, Llanet Tovar-Mora, José Ramón Pardons-Blas, Yvonne Herrerías-Diego, Rodolfo Pérez-Rodríguez and Ignacio Doadrio', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2
018, 11, 20, 13, 56, 45)), (21, 'Parallel identification of novel antimicrobial peptide sequences from multiple anuran species by targeted DNA sequencing', 'https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-018-5225-5', 'BMC Genomics', datetime.date
(2018, 11, 20), 'Authors: Tomislav Rončević, Marco Gerdol, Francesca Spazzali, Fiorella Florian, Stjepan Mekinić, Alessandro Tossi and Alberto Pallavicini', 'BMC', datetime.datetime(2018, 11, 20, 13, 29), datetime.datetime(2018, 11, 20, 13, 56, 45)))


def recursivePolling():
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(10)
        recursivePolling()

if __name__ == "__main__":
    recursivePolling()
