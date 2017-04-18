renthop.tr <- read.csv('/Users/adaezeajoku/Desktop/STATS415/Project/renthop_tr.csv')

renthop.te <- read.csv('/Users/adaezeajoku/Desktop/STATS415/Project/renthop_te.csv')

#' Step 0:

#' Step 1: Do as much data exploration as possible by visualization, summary statistics and perhaps a more sophisticated dimensionality reduction method such as PCA and/or MDS. 
#' 

#' how much time is a posting live for interest_level to be gauged? 1 week? Are they still live?

#' How many observations of each interest level are there?
table(renthop.tr$interest_level)
#' 7.8% high, 69.5% low, 22.8% medium

#' What is the distribution of price by interest level?
boxplot(price~interest_level, data=renthop.tr) #eliminate outliers!
tapply(renthop.tr$price, renthop.tr$interest_level, summary)
#' mean prices: high = 2700.293, low=4176.599, medium=3158.767
#' So people are more interested the lower the price.

#' How many words are in the description for each interest_level?
#' What is the lat/long for listings by interest_level? Are there clusters of regions by interest_level?
#' Are there certain undesirable managers?
#' Are there more/less desirable buildings?
#' What are typical features offered? By interest_level?

#' Which streets are most common in listings?
streets <- table(renthop.tr$display_address)
#' Broadway, East 34th Street, Second Ave

#' Does no photo translate to low interest?
table(renthop.tr$interest_level[renthop.tr$photos == '[]'])
#' Yes 95% of the time.

#' Do no features translate to low interest?
table(renthop.tr$interest_level[renthop.tr$features == '[]'])
#' Yes 65% of the time.

#' Add photo_count column and binary photo column (0/1)