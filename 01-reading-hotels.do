pwd
cd "C:\Users\Popa_Alexia\Documents\coding for economists"
mkdir "C:\Users\Popa_Alexia\Documents\coding for economists\data"

copy "C:\Users\Popa_Alexia\Documents\coding for economists\coding assignment\hotels-vienna.csv" "C:\Users\Popa_Alexia\Documents\coding for economists\data\hotels-vienna.csv"

import delimited "C:\Users\Popa_Alexia\Documents\coding for economists\coding assignment\hotels-vienna.csv", bindquote(strict) varnames(1) encoding(UTF-8) clear

*clean data*
describe
replace rating = "" if rating == "NA"
destring rating, replace

keep city_actual price stars distance accommodation_type rating
keep if accommodation_type == "Hotel"
drop if city_actual !="Vienna"

save "data\hotels-vienna.csv", replace