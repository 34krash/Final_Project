{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt\n",
    "import random \n",
    "import numpy\n",
    "from scipy import stats\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_2020 = pd.read_csv(\"Clean_Data/World_Happiness_2020.csv\")\n",
    "df_2019 = pd.read_csv(\"Clean_Data/World_Happiness_2019.csv\")\n",
    "df_2018 = pd.read_csv(\"Clean_Data/World_Happiness_2018.csv\")\n",
    "df_2017 = pd.read_csv(\"Clean_Data/World_Happiness_2017.csv\")\n",
    "df_2016 = pd.read_csv(\"Clean_Data/World_Happiness_2016.csv\")\n",
    "df_2015 = pd.read_csv(\"Clean_Data/World_Happiness_2015.csv\")\n",
    "df_country_lat_lon = pd.read_csv(\"Clean_Data/Countries_lat_lon.csv\", encoding='latin-1')\n",
    "df_economic_index = pd.read_csv(\"Clean_Data/economic_freedom_index2019_data.csv\", encoding='latin-1')\n",
    "df_corruption_index = pd.read_csv(\"Clean_Data/Corruption_perception_index.csv\", encoding='latin-1')\n",
    "df_life_expect_index = pd.read_csv(\"Clean_Data/Life_Expectancy_Data.csv\", encoding='latin-1')\n",
    "df_freedom_index = pd.read_csv(\"Clean_Data/Freedom_Index_08-17.csv\", encoding='latin-1')\n",
    "df_countries_index = pd.read_csv(\"Clean_Data/countries_of_the_world.csv\", encoding='latin-1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "coord_2019 = df_2019.merge(df_country_lat_lon, on='Country', how = 'inner')\n",
    "coord_2018 = df_2018.merge(df_country_lat_lon, on='Country', how = 'inner')\n",
    "coord_2017 = df_2017.merge(df_country_lat_lon, on='Country', how = 'inner')\n",
    "coord_2016 = df_2016.merge(df_country_lat_lon, on='Country', how = 'inner')\n",
    "coord_2015 = df_2015.merge(df_country_lat_lon, on='Country', how = 'inner')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "coord_2019.to_csv(r'Clean_Data/happiness_map2019.csv', index = False)\n",
    "coord_2018.to_csv(r'Clean_Data/happiness_map2018.csv', index = False)\n",
    "coord_2017.to_csv(r'Clean_Data/happiness_map2017.csv', index = False)\n",
    "coord_2016.to_csv(r'Clean_Data/happiness_map2016.csv', index = False)\n",
    "coord_2015.to_csv(r'Clean_Data/happiness_map2015.csv', index = False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'countries'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-9e8387c79127>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mhappiness_corruption\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf_corruption_index\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmerge\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf_2020\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mon\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'Country'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhow\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'inner'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mhappiness_life_expt\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf_life_expect_index\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmerge\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf_2020\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mon\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'Country'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhow\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'inner'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mhappiness_freedom\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf_freedom_index\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmerge\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf_2020\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mleft_on\u001b[0m \u001b[1;33m=\u001b[0m\u001b[1;34m'countries'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mright_on\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'Country'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhow\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'inner'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[0mhappiness_countries\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdf_countries_index\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmerge\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdf_2020\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mon\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'Country'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mhow\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'inner'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36mmerge\u001b[1;34m(self, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate)\u001b[0m\n\u001b[0;32m   7295\u001b[0m             \u001b[0mcopy\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcopy\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   7296\u001b[0m             \u001b[0mindicator\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mindicator\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 7297\u001b[1;33m             \u001b[0mvalidate\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mvalidate\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   7298\u001b[0m         )\n\u001b[0;32m   7299\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[0m in \u001b[0;36mmerge\u001b[1;34m(left, right, how, on, left_on, right_on, left_index, right_index, sort, suffixes, copy, indicator, validate)\u001b[0m\n\u001b[0;32m     84\u001b[0m         \u001b[0mcopy\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mcopy\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     85\u001b[0m         \u001b[0mindicator\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mindicator\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 86\u001b[1;33m         \u001b[0mvalidate\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mvalidate\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     87\u001b[0m     )\n\u001b[0;32m     88\u001b[0m     \u001b[1;32mreturn\u001b[0m \u001b[0mop\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_result\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[0m in \u001b[0;36m__init__\u001b[1;34m(self, left, right, how, on, left_on, right_on, axis, left_index, right_index, sort, suffixes, copy, indicator, validate)\u001b[0m\n\u001b[0;32m    625\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mright_join_keys\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    626\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mjoin_names\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 627\u001b[1;33m         ) = self._get_merge_keys()\n\u001b[0m\u001b[0;32m    628\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    629\u001b[0m         \u001b[1;31m# validate the merge keys dtypes. We may need to coerce\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\pandas\\core\\reshape\\merge.py\u001b[0m in \u001b[0;36m_get_merge_keys\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    994\u001b[0m                         \u001b[0mright_keys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mrk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    995\u001b[0m                     \u001b[1;32mif\u001b[0m \u001b[0mlk\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 996\u001b[1;33m                         \u001b[0mleft_keys\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mleft\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_label_or_level_values\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    997\u001b[0m                         \u001b[0mjoin_names\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlk\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    998\u001b[0m                     \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\envs\\PythonData\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36m_get_label_or_level_values\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1690\u001b[0m             \u001b[0mvalues\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0maxes\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_level_values\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_values\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1691\u001b[0m         \u001b[1;32melse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 1692\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   1693\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   1694\u001b[0m         \u001b[1;31m# Check for duplicates\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'countries'"
     ]
    }
   ],
   "source": [
    "happiness_econ = df_economic_index.merge(df_2020, left_on ='Country Name', right_on = 'Country', how = 'inner')\n",
    "happiness_corruption = df_corruption_index.merge(df_2020, on = 'Country', how = 'inner')\n",
    "happiness_life_expt = df_life_expect_index.merge(df_2020, on = 'Country', how = 'inner')\n",
    "happiness_freedom = df_freedom_index.merge(df_2020, left_on = 'countries', right_on = 'Country', how = 'inner')\n",
    "happiness_countries = df_countries_index.merge(df_2020, on = 'Country', how = 'inner')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData] *",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
