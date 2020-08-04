{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As part of a UNICEF project whose mission is to improve the well-being of children around the world,\n",
    "it is necessary to track the impact of students' living conditions between the ages of 15 and 22 on their math score in order to identify at-risk students at an early stage."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Importing libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from itertools import combinations\n",
    "from scipy.stats import ttest_ind\n",
    "\n",
    "pd.set_option('display.max_rows', 50)\n",
    "pd.set_option('display.max_columns', 50)\n",
    "\n",
    "students = pd.read_csv('stud_math.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>school</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>Pstatus</th>\n",
       "      <th>Medu</th>\n",
       "      <th>Fedu</th>\n",
       "      <th>Mjob</th>\n",
       "      <th>Fjob</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>schoolsup</th>\n",
       "      <th>famsup</th>\n",
       "      <th>paid</th>\n",
       "      <th>activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>studytime, granular</th>\n",
       "      <th>higher</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>famrel</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>teacher</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>health</td>\n",
       "      <td>NaN</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>-9.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>services</td>\n",
       "      <td>other</td>\n",
       "      <td>reputation</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>16</td>\n",
       "      <td>NaN</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>55.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>A</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>other</td>\n",
       "      <td>teacher</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>A</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>services</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>95.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>-6.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  school sex  age address famsize Pstatus  Medu  Fedu      Mjob     Fjob  \\\n",
       "0     GP   F   18       U     NaN       A   4.0   4.0   at_home  teacher   \n",
       "1     GP   F   17       U     GT3     NaN   1.0   1.0   at_home    other   \n",
       "2     GP   F   15       U     LE3       T   1.0   1.0   at_home    other   \n",
       "3     GP   F   15       U     GT3       T   4.0   2.0    health      NaN   \n",
       "4     GP   F   16       U     GT3       T   3.0   3.0     other    other   \n",
       "5     GP   M   16       U     LE3       T   4.0   3.0  services    other   \n",
       "6     GP   M   16     NaN     LE3       T   2.0   2.0     other    other   \n",
       "7     GP   F   17       U     GT3       A   4.0   4.0     other  teacher   \n",
       "8     GP   M   15       U     LE3       A   3.0   2.0  services    other   \n",
       "9     GP   M   15       U     NaN     NaN   3.0   4.0     other    other   \n",
       "\n",
       "       reason guardian  traveltime  studytime  failures schoolsup famsup paid  \\\n",
       "0      course   mother         2.0        2.0       0.0       yes     no   no   \n",
       "1      course   father         1.0        2.0       0.0        no    yes   no   \n",
       "2       other   mother         1.0        2.0       3.0       yes     no  NaN   \n",
       "3        home   mother         1.0        3.0       0.0        no    yes  yes   \n",
       "4        home   father         1.0        2.0       0.0        no    yes  yes   \n",
       "5  reputation   mother         1.0        2.0       0.0        no    yes  yes   \n",
       "6        home   mother         1.0        2.0       0.0        no     no   no   \n",
       "7        home   mother         2.0        2.0       0.0       yes    yes   no   \n",
       "8        home   mother         1.0        2.0       0.0        no    yes  yes   \n",
       "9        home   mother         1.0        2.0       0.0        no    yes  yes   \n",
       "\n",
       "  activities nursery  studytime, granular higher internet romantic  famrel  \\\n",
       "0         no     yes                 -6.0    yes      NaN       no     4.0   \n",
       "1         no      no                 -6.0    yes      yes       no     5.0   \n",
       "2         no     yes                 -6.0    yes      yes      NaN     4.0   \n",
       "3        yes     yes                 -9.0    yes      yes      yes     3.0   \n",
       "4         no     yes                 -6.0    yes       no       no     4.0   \n",
       "5        yes     yes                 -6.0    yes      yes       no     5.0   \n",
       "6         no     yes                 -6.0    yes      yes       no     4.0   \n",
       "7         no     yes                 -6.0    yes       no       no     4.0   \n",
       "8         no     yes                 -6.0    yes      yes       no     NaN   \n",
       "9        yes     yes                 -6.0    yes      yes       no     5.0   \n",
       "\n",
       "   freetime  goout  health  absences  score  \n",
       "0       3.0    4.0     3.0       6.0   30.0  \n",
       "1       3.0    3.0     3.0       4.0   30.0  \n",
       "2       3.0    2.0     3.0      10.0   50.0  \n",
       "3       2.0    2.0     5.0       2.0   75.0  \n",
       "4       3.0    2.0     5.0       4.0   50.0  \n",
       "5       4.0    2.0     5.0      10.0   75.0  \n",
       "6       4.0    4.0     3.0       0.0   55.0  \n",
       "7       1.0    4.0     1.0       6.0   30.0  \n",
       "8       2.0    2.0     1.0       0.0   95.0  \n",
       "9       5.0    1.0     5.0       0.0   75.0  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 395 entries, 0 to 394\n",
      "Data columns (total 30 columns):\n",
      " #   Column               Non-Null Count  Dtype  \n",
      "---  ------               --------------  -----  \n",
      " 0   school               395 non-null    object \n",
      " 1   sex                  395 non-null    object \n",
      " 2   age                  395 non-null    int64  \n",
      " 3   address              378 non-null    object \n",
      " 4   famsize              368 non-null    object \n",
      " 5   Pstatus              350 non-null    object \n",
      " 6   Medu                 392 non-null    float64\n",
      " 7   Fedu                 371 non-null    float64\n",
      " 8   Mjob                 376 non-null    object \n",
      " 9   Fjob                 359 non-null    object \n",
      " 10  reason               378 non-null    object \n",
      " 11  guardian             364 non-null    object \n",
      " 12  traveltime           367 non-null    float64\n",
      " 13  studytime            388 non-null    float64\n",
      " 14  failures             373 non-null    float64\n",
      " 15  schoolsup            386 non-null    object \n",
      " 16  famsup               356 non-null    object \n",
      " 17  paid                 355 non-null    object \n",
      " 18  activities           381 non-null    object \n",
      " 19  nursery              379 non-null    object \n",
      " 20  studytime, granular  388 non-null    float64\n",
      " 21  higher               375 non-null    object \n",
      " 22  internet             361 non-null    object \n",
      " 23  romantic             364 non-null    object \n",
      " 24  famrel               368 non-null    float64\n",
      " 25  freetime             384 non-null    float64\n",
      " 26  goout                387 non-null    float64\n",
      " 27  health               380 non-null    float64\n",
      " 28  absences             383 non-null    float64\n",
      " 29  score                389 non-null    float64\n",
      "dtypes: float64(12), int64(1), object(17)\n",
      "memory usage: 92.7+ KB\n"
     ]
    }
   ],
   "source": [
    "students.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "So we have one dataset with 30 columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>Medu</th>\n",
       "      <th>Fedu</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>studytime, granular</th>\n",
       "      <th>famrel</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>395.000000</td>\n",
       "      <td>392.000000</td>\n",
       "      <td>371.000000</td>\n",
       "      <td>367.000000</td>\n",
       "      <td>388.000000</td>\n",
       "      <td>373.000000</td>\n",
       "      <td>388.000000</td>\n",
       "      <td>368.000000</td>\n",
       "      <td>384.000000</td>\n",
       "      <td>387.000000</td>\n",
       "      <td>380.000000</td>\n",
       "      <td>383.000000</td>\n",
       "      <td>389.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>16.696203</td>\n",
       "      <td>2.750000</td>\n",
       "      <td>2.614555</td>\n",
       "      <td>1.438692</td>\n",
       "      <td>2.038660</td>\n",
       "      <td>0.337802</td>\n",
       "      <td>-6.115979</td>\n",
       "      <td>3.937500</td>\n",
       "      <td>3.231771</td>\n",
       "      <td>3.105943</td>\n",
       "      <td>3.531579</td>\n",
       "      <td>7.279373</td>\n",
       "      <td>52.262211</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.276043</td>\n",
       "      <td>1.098127</td>\n",
       "      <td>2.228732</td>\n",
       "      <td>0.694181</td>\n",
       "      <td>0.842078</td>\n",
       "      <td>0.743135</td>\n",
       "      <td>2.526235</td>\n",
       "      <td>0.927277</td>\n",
       "      <td>0.993940</td>\n",
       "      <td>1.115896</td>\n",
       "      <td>1.396019</td>\n",
       "      <td>23.465197</td>\n",
       "      <td>22.919022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-12.000000</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>16.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-6.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-6.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>55.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>70.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>22.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>-3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>385.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              age        Medu        Fedu  traveltime   studytime    failures  \\\n",
       "count  395.000000  392.000000  371.000000  367.000000  388.000000  373.000000   \n",
       "mean    16.696203    2.750000    2.614555    1.438692    2.038660    0.337802   \n",
       "std      1.276043    1.098127    2.228732    0.694181    0.842078    0.743135   \n",
       "min     15.000000    0.000000    0.000000    1.000000    1.000000    0.000000   \n",
       "25%     16.000000    2.000000    2.000000    1.000000    1.000000    0.000000   \n",
       "50%     17.000000    3.000000    2.000000    1.000000    2.000000    0.000000   \n",
       "75%     18.000000    4.000000    3.000000    2.000000    2.000000    0.000000   \n",
       "max     22.000000    4.000000   40.000000    4.000000    4.000000    3.000000   \n",
       "\n",
       "       studytime, granular      famrel    freetime       goout      health  \\\n",
       "count           388.000000  368.000000  384.000000  387.000000  380.000000   \n",
       "mean             -6.115979    3.937500    3.231771    3.105943    3.531579   \n",
       "std               2.526235    0.927277    0.993940    1.115896    1.396019   \n",
       "min             -12.000000   -1.000000    1.000000    1.000000    1.000000   \n",
       "25%              -6.000000    4.000000    3.000000    2.000000    3.000000   \n",
       "50%              -6.000000    4.000000    3.000000    3.000000    4.000000   \n",
       "75%              -3.000000    5.000000    4.000000    4.000000    5.000000   \n",
       "max              -3.000000    5.000000    5.000000    5.000000    5.000000   \n",
       "\n",
       "         absences       score  \n",
       "count  383.000000  389.000000  \n",
       "mean     7.279373   52.262211  \n",
       "std     23.465197   22.919022  \n",
       "min      0.000000    0.000000  \n",
       "25%      0.000000   40.000000  \n",
       "50%      4.000000   55.000000  \n",
       "75%      8.000000   70.000000  \n",
       "max    385.000000  100.000000  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The column names don't make it clear what they mean, so they'll be renamed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu',\n",
       "       'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime',\n",
       "       'failures', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery',\n",
       "       'studytime, granular', 'higher', 'internet', 'romantic', 'famrel',\n",
       "       'freetime', 'goout', 'health', 'absences', 'score'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "students.columns = ['school', 'sex', 'age', 'address', 'famsize', 'parents_status', 'mother_education', 'father_education', 'mother_job',\n",
    "                    'father_job', 'reason', 'guardian', 'traveltime', 'studytime', 'failures',\n",
    "                    'school_suppport', 'family_support', 'paid_additional_classes', 'additional_activities', 'nursery', 'studytime, granular', 'higher_education',\n",
    "                    'internet', 'romantic', 'family_relationship', 'freetime', 'goout', 'health',\n",
    "                    'absences', 'score']"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First let's check whether there are any duplicates in the presented dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False    395\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.duplicated().value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "No duplicated rows"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Most of columns have missing data, which is normal in real world. Also there are some continuous variables and some categorical. Let's have a closer look at them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "To perform the analysis, we'll divide all the columns into nominative and numerical ones"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['age', 'mother_education', 'father_education', 'traveltime', 'studytime', 'failures', 'studytime, granular', 'family_relationship', 'freetime', 'goout', 'health', 'absences', 'score']\n",
      "['school', 'sex', 'address', 'famsize', 'parents_status', 'mother_job', 'father_job', 'reason', 'guardian', 'school_suppport', 'family_support', 'paid_additional_classes', 'additional_activities', 'nursery', 'higher_education', 'internet', 'romantic']\n"
     ]
    }
   ],
   "source": [
    "list_of_numeric = students.select_dtypes(np.number).columns.tolist()\n",
    "print(list_of_numeric)\n",
    "\n",
    "list_of_nominative = students.select_dtypes('object').columns.tolist()\n",
    "print(list_of_nominative)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It should be noted that despite the fact that some data were assigned to numerical data by this method, they are nominative in their meaning and will be analyzed accordingly"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Analysis of numeric columns\n",
    "\n",
    "Let's start with the main column - 'score'. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "50.0     54\n",
       "55.0     46\n",
       "0.0      37\n",
       "75.0     33\n",
       "65.0     31\n",
       "40.0     31\n",
       "60.0     31\n",
       "45.0     27\n",
       "70.0     27\n",
       "80.0     16\n",
       "30.0     15\n",
       "90.0     12\n",
       "35.0      9\n",
       "25.0      7\n",
       "NaN       6\n",
       "85.0      6\n",
       "95.0      5\n",
       "100.0     1\n",
       "20.0      1\n",
       "Name: score, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['score'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since we have missing values in this column, this will not allow us to analyze them, and it is pointless to fill in the data with other values, because this may affect the final conclusions. In addition, there are too few missing values, so we delete them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "students = students[~students['score'].isnull()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 389 entries, 0 to 394\n",
      "Data columns (total 30 columns):\n",
      " #   Column                   Non-Null Count  Dtype  \n",
      "---  ------                   --------------  -----  \n",
      " 0   school                   389 non-null    object \n",
      " 1   sex                      389 non-null    object \n",
      " 2   age                      389 non-null    int64  \n",
      " 3   address                  374 non-null    object \n",
      " 4   famsize                  362 non-null    object \n",
      " 5   parents_status           344 non-null    object \n",
      " 6   mother_education         386 non-null    float64\n",
      " 7   father_education         365 non-null    float64\n",
      " 8   mother_job               370 non-null    object \n",
      " 9   father_job               353 non-null    object \n",
      " 10  reason                   372 non-null    object \n",
      " 11  guardian                 358 non-null    object \n",
      " 12  traveltime               361 non-null    float64\n",
      " 13  studytime                382 non-null    float64\n",
      " 14  failures                 367 non-null    float64\n",
      " 15  school_suppport          380 non-null    object \n",
      " 16  family_support           351 non-null    object \n",
      " 17  paid_additional_classes  350 non-null    object \n",
      " 18  additional_activities    375 non-null    object \n",
      " 19  nursery                  374 non-null    object \n",
      " 20  studytime, granular      382 non-null    float64\n",
      " 21  higher_education         369 non-null    object \n",
      " 22  internet                 355 non-null    object \n",
      " 23  romantic                 358 non-null    object \n",
      " 24  family_relationship      362 non-null    float64\n",
      " 25  freetime                 380 non-null    float64\n",
      " 26  goout                    382 non-null    float64\n",
      " 27  health                   374 non-null    float64\n",
      " 28  absences                 378 non-null    float64\n",
      " 29  score                    389 non-null    float64\n",
      "dtypes: float64(12), int64(1), object(17)\n",
      "memory usage: 94.2+ KB\n"
     ]
    }
   ],
   "source": [
    "students.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1e5cd8f5448>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1008x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "correlation = students.corr()\n",
    "plt.figure(figsize=(14, 8))\n",
    "sns.heatmap(correlation, annot=True, cmap='coolwarm')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We don't have data about the column 'studytime, granular' in the terms of reference. In addition, this column is completely negatively correlated with the column 'studytime', so we delete the column 'studytime, granular' ."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "students.drop(['studytime, granular'], inplace=True, axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's look at the column 'age' and figure out is there students older than 22 or younger then 15, wich is not appropiate with our conditions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    389.000000\n",
       "mean      16.673522\n",
       "std        1.265662\n",
       "min       15.000000\n",
       "25%       16.000000\n",
       "50%       17.000000\n",
       "75%       18.000000\n",
       "max       22.000000\n",
       "Name: age, dtype: float64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.age.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The data meets the conditions, we will check them for outliers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1e5cda3ba88>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "students.boxplot(column=['age'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def find_outliers(x):  # Function to show boundaries of outliers\n",
    "    if x.dtype == 'int64' or x.dtype == 'float64':\n",
    "        print('25th percentile: {},'.format(x.quantile(0.25)),\n",
    "              '75th percentile: {},'.format(x.quantile(0.75)),\n",
    "              \"IQR: {}, \".format(x.quantile(\n",
    "                  0.75) - x.quantile(0.25)),\n",
    "              \"The boundaries of outliers: [{f}, {l}].\".format(f=(x.quantile(0.25)) - 1.5*(x.quantile(0.75) - x.quantile(0.25)), l=(x.quantile(0.75)) + 1.5*(x.quantile(0.75) - x.quantile(0.25))))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25th percentile: 16.0, 75th percentile: 18.0, IQR: 2.0,  The boundaries of outliers: [13.0, 21.0].\n"
     ]
    }
   ],
   "source": [
    "find_outliers(students.age)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have two outliers in dataset, let's look at them closer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>school</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>parents_status</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>mother_job</th>\n",
       "      <th>father_job</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>school_suppport</th>\n",
       "      <th>family_support</th>\n",
       "      <th>paid_additional_classes</th>\n",
       "      <th>additional_activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>higher_education</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>family_relationship</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>392</th>\n",
       "      <td>MS</td>\n",
       "      <td>M</td>\n",
       "      <td>21</td>\n",
       "      <td>R</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    school sex  age address famsize parents_status  mother_education  \\\n",
       "392     MS   M   21       R     GT3              T               1.0   \n",
       "\n",
       "     father_education mother_job father_job  reason guardian  traveltime  \\\n",
       "392               1.0      other      other  course      NaN         1.0   \n",
       "\n",
       "     studytime  failures school_suppport family_support  \\\n",
       "392        1.0       3.0             NaN             no   \n",
       "\n",
       "    paid_additional_classes additional_activities nursery higher_education  \\\n",
       "392                      no                    no      no              NaN   \n",
       "\n",
       "    internet romantic  family_relationship  freetime  goout  health  absences  \\\n",
       "392       no       no                  5.0       5.0    3.0     3.0       3.0   \n",
       "\n",
       "     score  \n",
       "392   35.0  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students[students['age'] == 21]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>family_relationship</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>389.000000</td>\n",
       "      <td>386.000000</td>\n",
       "      <td>365.000000</td>\n",
       "      <td>361.000000</td>\n",
       "      <td>382.000000</td>\n",
       "      <td>367.000000</td>\n",
       "      <td>362.000000</td>\n",
       "      <td>380.000000</td>\n",
       "      <td>382.000000</td>\n",
       "      <td>374.000000</td>\n",
       "      <td>378.000000</td>\n",
       "      <td>389.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>16.673522</td>\n",
       "      <td>2.766839</td>\n",
       "      <td>2.627397</td>\n",
       "      <td>1.434903</td>\n",
       "      <td>2.036649</td>\n",
       "      <td>0.326975</td>\n",
       "      <td>3.930939</td>\n",
       "      <td>3.223684</td>\n",
       "      <td>3.094241</td>\n",
       "      <td>3.529412</td>\n",
       "      <td>7.320106</td>\n",
       "      <td>52.262211</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.265662</td>\n",
       "      <td>1.094277</td>\n",
       "      <td>2.241790</td>\n",
       "      <td>0.692660</td>\n",
       "      <td>0.847239</td>\n",
       "      <td>0.729479</td>\n",
       "      <td>0.931554</td>\n",
       "      <td>0.993364</td>\n",
       "      <td>1.116104</td>\n",
       "      <td>1.402006</td>\n",
       "      <td>23.615525</td>\n",
       "      <td>22.919022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>-1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>16.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>55.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>70.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>22.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>40.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>385.000000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              age  mother_education  father_education  traveltime   studytime  \\\n",
       "count  389.000000        386.000000        365.000000  361.000000  382.000000   \n",
       "mean    16.673522          2.766839          2.627397    1.434903    2.036649   \n",
       "std      1.265662          1.094277          2.241790    0.692660    0.847239   \n",
       "min     15.000000          0.000000          0.000000    1.000000    1.000000   \n",
       "25%     16.000000          2.000000          2.000000    1.000000    1.000000   \n",
       "50%     17.000000          3.000000          3.000000    1.000000    2.000000   \n",
       "75%     18.000000          4.000000          3.000000    2.000000    2.000000   \n",
       "max     22.000000          4.000000         40.000000    4.000000    4.000000   \n",
       "\n",
       "         failures  family_relationship    freetime       goout      health  \\\n",
       "count  367.000000           362.000000  380.000000  382.000000  374.000000   \n",
       "mean     0.326975             3.930939    3.223684    3.094241    3.529412   \n",
       "std      0.729479             0.931554    0.993364    1.116104    1.402006   \n",
       "min      0.000000            -1.000000    1.000000    1.000000    1.000000   \n",
       "25%      0.000000             4.000000    3.000000    2.000000    3.000000   \n",
       "50%      0.000000             4.000000    3.000000    3.000000    4.000000   \n",
       "75%      0.000000             5.000000    4.000000    4.000000    5.000000   \n",
       "max      3.000000             5.000000    5.000000    5.000000    5.000000   \n",
       "\n",
       "         absences       score  \n",
       "count  378.000000  389.000000  \n",
       "mean     7.320106   52.262211  \n",
       "std     23.615525   22.919022  \n",
       "min      0.000000    0.000000  \n",
       "25%      0.000000   40.000000  \n",
       "50%      4.000000   55.000000  \n",
       "75%      8.000000   70.000000  \n",
       "max    385.000000  100.000000  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25th percentile: 40.0, 75th percentile: 70.0, IQR: 30.0,  The boundaries of outliers: [-5.0, 115.0].\n"
     ]
    }
   ],
   "source": [
    "find_outliers(students.score)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, these outliers do not affect the appearance of outliers in the tolerable column 'score', and since they fit the specified conditions, so that if they are deleted, the conditions will not be met, we leave these values. For the purpose not deleting them, we'll now fill empty values in this row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mother    248\n",
       "father     86\n",
       "other      24\n",
       "Name: guardian, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['guardian'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     331\n",
       "yes     49\n",
       "Name: school_suppport, dtype: int64"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['school_suppport'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "yes    350\n",
       "no      19\n",
       "Name: higher_education, dtype: int64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['higher_education'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "students.loc[students.age == 21, 'guardian'] = 'mother'\n",
    "students.loc[students.age == 21, 'school_suppport'] = 'no'\n",
    "students.loc[students.age == 21, 'higher_education'] = 'yes'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>school</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>parents_status</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>mother_job</th>\n",
       "      <th>father_job</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>school_suppport</th>\n",
       "      <th>family_support</th>\n",
       "      <th>paid_additional_classes</th>\n",
       "      <th>additional_activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>higher_education</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>family_relationship</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>392</th>\n",
       "      <td>MS</td>\n",
       "      <td>M</td>\n",
       "      <td>21</td>\n",
       "      <td>R</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    school sex  age address famsize parents_status  mother_education  \\\n",
       "392     MS   M   21       R     GT3              T               1.0   \n",
       "\n",
       "     father_education mother_job father_job  reason guardian  traveltime  \\\n",
       "392               1.0      other      other  course   mother         1.0   \n",
       "\n",
       "     studytime  failures school_suppport family_support  \\\n",
       "392        1.0       3.0              no             no   \n",
       "\n",
       "    paid_additional_classes additional_activities nursery higher_education  \\\n",
       "392                      no                    no      no              yes   \n",
       "\n",
       "    internet romantic  family_relationship  freetime  goout  health  absences  \\\n",
       "392       no       no                  5.0       5.0    3.0     3.0       3.0   \n",
       "\n",
       "     score  \n",
       "392   35.0  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students[students['age'] == 21]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>school</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>parents_status</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>mother_job</th>\n",
       "      <th>father_job</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>school_suppport</th>\n",
       "      <th>family_support</th>\n",
       "      <th>paid_additional_classes</th>\n",
       "      <th>additional_activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>higher_education</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>family_relationship</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>teacher</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>health</td>\n",
       "      <td>NaN</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  school sex  age address famsize parents_status  mother_education  \\\n",
       "0     GP   F   18       U     NaN              A               4.0   \n",
       "1     GP   F   17       U     GT3            NaN               1.0   \n",
       "2     GP   F   15       U     LE3              T               1.0   \n",
       "3     GP   F   15       U     GT3              T               4.0   \n",
       "4     GP   F   16       U     GT3              T               3.0   \n",
       "\n",
       "   father_education mother_job father_job  reason guardian  traveltime  \\\n",
       "0               4.0    at_home    teacher  course   mother         2.0   \n",
       "1               1.0    at_home      other  course   father         1.0   \n",
       "2               1.0    at_home      other   other   mother         1.0   \n",
       "3               2.0     health        NaN    home   mother         1.0   \n",
       "4               3.0      other      other    home   father         1.0   \n",
       "\n",
       "   studytime  failures school_suppport family_support paid_additional_classes  \\\n",
       "0        2.0       0.0             yes             no                      no   \n",
       "1        2.0       0.0              no            yes                      no   \n",
       "2        2.0       3.0             yes             no                     NaN   \n",
       "3        3.0       0.0              no            yes                     yes   \n",
       "4        2.0       0.0              no            yes                     yes   \n",
       "\n",
       "  additional_activities nursery higher_education internet romantic  \\\n",
       "0                    no     yes              yes      NaN       no   \n",
       "1                    no      no              yes      yes       no   \n",
       "2                    no     yes              yes      yes      NaN   \n",
       "3                   yes     yes              yes      yes      yes   \n",
       "4                    no     yes              yes       no       no   \n",
       "\n",
       "   family_relationship  freetime  goout  health  absences  score  \n",
       "0                  4.0       3.0    4.0     3.0       6.0   30.0  \n",
       "1                  5.0       3.0    3.0     3.0       4.0   30.0  \n",
       "2                  4.0       3.0    2.0     3.0      10.0   50.0  \n",
       "3                  3.0       2.0    2.0     5.0       2.0   75.0  \n",
       "4                  4.0       3.0    2.0     5.0       4.0   50.0  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0    131\n",
       "2.0    100\n",
       "3.0     96\n",
       "1.0     56\n",
       "0.0      3\n",
       "NaN      3\n",
       "Name: mother_education, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.mother_education.value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we have only 2 missed values, we'll fill them with mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "students.mother_education.value_counts()\n",
    "students['mother_education'] = students['mother_education'].fillna(\n",
    "    students.mother_education.median())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we coul see earlier, values of column 'mother_education' are highly correlated with values of column 'father_education', so we can fill empty values of the last one with those in first one."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['father_education'] = students['father_education'].fillna(\n",
    "    students['mother_education'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's check the result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 389 entries, 0 to 394\n",
      "Data columns (total 29 columns):\n",
      " #   Column                   Non-Null Count  Dtype  \n",
      "---  ------                   --------------  -----  \n",
      " 0   school                   389 non-null    object \n",
      " 1   sex                      389 non-null    object \n",
      " 2   age                      389 non-null    int64  \n",
      " 3   address                  374 non-null    object \n",
      " 4   famsize                  362 non-null    object \n",
      " 5   parents_status           344 non-null    object \n",
      " 6   mother_education         389 non-null    float64\n",
      " 7   father_education         389 non-null    float64\n",
      " 8   mother_job               370 non-null    object \n",
      " 9   father_job               353 non-null    object \n",
      " 10  reason                   372 non-null    object \n",
      " 11  guardian                 359 non-null    object \n",
      " 12  traveltime               361 non-null    float64\n",
      " 13  studytime                382 non-null    float64\n",
      " 14  failures                 367 non-null    float64\n",
      " 15  school_suppport          381 non-null    object \n",
      " 16  family_support           351 non-null    object \n",
      " 17  paid_additional_classes  350 non-null    object \n",
      " 18  additional_activities    375 non-null    object \n",
      " 19  nursery                  374 non-null    object \n",
      " 20  higher_education         370 non-null    object \n",
      " 21  internet                 355 non-null    object \n",
      " 22  romantic                 358 non-null    object \n",
      " 23  family_relationship      362 non-null    float64\n",
      " 24  freetime                 380 non-null    float64\n",
      " 25  goout                    382 non-null    float64\n",
      " 26  health                   374 non-null    float64\n",
      " 27  absences                 378 non-null    float64\n",
      " 28  score                    389 non-null    float64\n",
      "dtypes: float64(11), int64(1), object(17)\n",
      "memory usage: 91.2+ KB\n"
     ]
    }
   ],
   "source": [
    "students.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0     109\n",
       "3.0     101\n",
       "4.0      98\n",
       "1.0      78\n",
       "0.0       2\n",
       "40.0      1\n",
       "Name: father_education, dtype: int64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.father_education.value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see an unappropriate value, so we'll delete this row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "students = students.loc[students['father_education'] != 40.0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25th percentile: 2.0, 75th percentile: 4.0, IQR: 2.0,  The boundaries of outliers: [-1.0, 7.0].\n",
      "25th percentile: 2.0, 75th percentile: 4.0, IQR: 2.0,  The boundaries of outliers: [-1.0, 7.0].\n"
     ]
    }
   ],
   "source": [
    "find_outliers(students.father_education)\n",
    "find_outliers(students.mother_education)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we see in these two columns no outliers\n",
    "\n",
    "Let's check other columns and fill null values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0    239\n",
       "2.0     94\n",
       "NaN     28\n",
       "3.0     20\n",
       "4.0      7\n",
       "Name: traveltime, dtype: int64"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['traveltime'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25th percentile: 1.0, 75th percentile: 2.0, IQR: 1.0,  The boundaries of outliers: [-0.5, 3.5].\n"
     ]
    }
   ],
   "source": [
    "find_outliers(students.traveltime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>school</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>parents_status</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>mother_job</th>\n",
       "      <th>father_job</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>school_suppport</th>\n",
       "      <th>family_support</th>\n",
       "      <th>paid_additional_classes</th>\n",
       "      <th>additional_activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>higher_education</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>family_relationship</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>61</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>services</td>\n",
       "      <td>services</td>\n",
       "      <td>course</td>\n",
       "      <td>father</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>55.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>108</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>15</td>\n",
       "      <td>R</td>\n",
       "      <td>GT3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>father</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>65.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>services</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>164</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>17</td>\n",
       "      <td>R</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>other</td>\n",
       "      <td>services</td>\n",
       "      <td>course</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.0</td>\n",
       "      <td>35.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>228</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>NaN</td>\n",
       "      <td>T</td>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>14.0</td>\n",
       "      <td>45.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>327</th>\n",
       "      <td>GP</td>\n",
       "      <td>M</td>\n",
       "      <td>17</td>\n",
       "      <td>R</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>services</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>8.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>375</th>\n",
       "      <td>MS</td>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>R</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    school sex  age address famsize parents_status  mother_education  \\\n",
       "61      GP   F   16       U     GT3              T               1.0   \n",
       "108     GP   M   15       R     GT3            NaN               4.0   \n",
       "149     GP   M   15       U     LE3            NaN               2.0   \n",
       "164     GP   M   17       R     LE3              T               1.0   \n",
       "228     GP   M   18       U     NaN              T               2.0   \n",
       "327     GP   M   17       R     GT3              T               2.0   \n",
       "375     MS   F   18       R     GT3              T               1.0   \n",
       "\n",
       "     father_education mother_job father_job  reason guardian  traveltime  \\\n",
       "61                1.0   services   services  course   father         4.0   \n",
       "108               4.0      other      other    home   father         4.0   \n",
       "149               1.0   services      other  course   mother         4.0   \n",
       "164               1.0      other   services  course      NaN         4.0   \n",
       "228               1.0    at_home      other  course   mother         4.0   \n",
       "327               2.0   services      other  course   mother         4.0   \n",
       "375               1.0      other      other    home   mother         4.0   \n",
       "\n",
       "     studytime  failures school_suppport family_support  \\\n",
       "61         1.0       0.0             yes            NaN   \n",
       "108        4.0       NaN              no            yes   \n",
       "149        1.0       3.0              no            NaN   \n",
       "164        2.0       3.0              no             no   \n",
       "228        2.0       0.0             yes            yes   \n",
       "327        1.0       0.0              no            NaN   \n",
       "375        3.0       0.0              no             no   \n",
       "\n",
       "    paid_additional_classes additional_activities nursery higher_education  \\\n",
       "61                       no                   yes      no              yes   \n",
       "108                     yes                   yes     yes              yes   \n",
       "149                      no                    no     yes              NaN   \n",
       "164                     NaN                   yes     yes               no   \n",
       "228                     yes                   yes     yes              yes   \n",
       "327                      no                    no     yes              yes   \n",
       "375                      no                    no     yes              yes   \n",
       "\n",
       "    internet romantic  family_relationship  freetime  goout  health  absences  \\\n",
       "61       yes      yes                  5.0       5.0    5.0     5.0       6.0   \n",
       "108      yes      yes                  1.0       3.0    5.0     1.0       6.0   \n",
       "149      yes       no                  4.0       5.0    5.0     5.0       0.0   \n",
       "164       no      yes                  5.0       3.0    5.0     NaN       0.0   \n",
       "228      yes      yes                  4.0       3.0    2.0     3.0      14.0   \n",
       "327      yes       no                  4.0       4.0    5.0     4.0       8.0   \n",
       "375      yes       no                  4.0       3.0    2.0     4.0       2.0   \n",
       "\n",
       "     score  \n",
       "61    55.0  \n",
       "108   65.0  \n",
       "149   50.0  \n",
       "164   35.0  \n",
       "228   45.0  \n",
       "327   50.0  \n",
       "375   50.0  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students[students['traveltime'] > 3.5]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we see these outliers don't have much influence on the appearance of values in column 'score', so we leave them"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['traveltime'] = students['traveltime'].fillna(\n",
    "    students.traveltime.median())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 388 entries, 0 to 394\n",
      "Data columns (total 29 columns):\n",
      " #   Column                   Non-Null Count  Dtype  \n",
      "---  ------                   --------------  -----  \n",
      " 0   school                   388 non-null    object \n",
      " 1   sex                      388 non-null    object \n",
      " 2   age                      388 non-null    int64  \n",
      " 3   address                  373 non-null    object \n",
      " 4   famsize                  361 non-null    object \n",
      " 5   parents_status           344 non-null    object \n",
      " 6   mother_education         388 non-null    float64\n",
      " 7   father_education         388 non-null    float64\n",
      " 8   mother_job               369 non-null    object \n",
      " 9   father_job               352 non-null    object \n",
      " 10  reason                   371 non-null    object \n",
      " 11  guardian                 358 non-null    object \n",
      " 12  traveltime               388 non-null    float64\n",
      " 13  studytime                381 non-null    float64\n",
      " 14  failures                 366 non-null    float64\n",
      " 15  school_suppport          380 non-null    object \n",
      " 16  family_support           350 non-null    object \n",
      " 17  paid_additional_classes  349 non-null    object \n",
      " 18  additional_activities    374 non-null    object \n",
      " 19  nursery                  373 non-null    object \n",
      " 20  higher_education         369 non-null    object \n",
      " 21  internet                 354 non-null    object \n",
      " 22  romantic                 357 non-null    object \n",
      " 23  family_relationship      361 non-null    float64\n",
      " 24  freetime                 379 non-null    float64\n",
      " 25  goout                    381 non-null    float64\n",
      " 26  health                   373 non-null    float64\n",
      " 27  absences                 377 non-null    float64\n",
      " 28  score                    388 non-null    float64\n",
      "dtypes: float64(11), int64(1), object(17)\n",
      "memory usage: 90.9+ KB\n"
     ]
    }
   ],
   "source": [
    "students.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0    289\n",
       "1.0     48\n",
       "NaN     22\n",
       "2.0     15\n",
       "3.0     14\n",
       "Name: failures, dtype: int64"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['failures'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['failures'] = students['failures'].fillna(students.failures.median())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1e5cdacdc48>"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "students.boxplot(column=['failures'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "failures\n",
       "0.0    56.109325\n",
       "1.0    40.000000\n",
       "2.0    32.333333\n",
       "3.0    29.642857\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='failures')['score'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we can see this column has an influence on the column 'Score' so we can't delete outliers. Besides, it is normal that it's not much students have a lot of failures "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0    189\n",
       "1.0    103\n",
       "3.0     62\n",
       "4.0     27\n",
       "NaN      7\n",
       "Name: studytime, dtype: int64"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['studytime'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25th percentile: 1.0, 75th percentile: 2.0, IQR: 1.0,  The boundaries of outliers: [-0.5, 3.5].\n"
     ]
    }
   ],
   "source": [
    "find_outliers(students.studytime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "studytime\n",
       "1.0    49.466019\n",
       "2.0    50.820106\n",
       "3.0    57.741935\n",
       "4.0    56.296296\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='studytime')['score'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we can see this column has an influence on the column 'Score' so we can't delete outliers. Besides, the difference between borders of outliers and outliers values is not big."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['studytime'] = students['studytime'].fillna(\n",
    "    students['studytime'].median())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       " 4.0    178\n",
       " 5.0     96\n",
       " 3.0     62\n",
       " NaN     27\n",
       " 2.0     17\n",
       " 1.0      7\n",
       "-1.0      1\n",
       "Name: family_relationship, dtype: int64"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['family_relationship'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see a mistake value here so we delete it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "students = students.loc[students['family_relationship'] != -1.0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25th percentile: 4.0, 75th percentile: 5.0, IQR: 1.0,  The boundaries of outliers: [2.5, 6.5].\n"
     ]
    }
   ],
   "source": [
    "find_outliers(students.family_relationship)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "family_relationship\n",
       "1.0    60.0\n",
       "2.0    55.0\n",
       "3.0    55.0\n",
       "4.0    52.5\n",
       "5.0    55.0\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='family_relationship')['score'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['family_relationship'] = students['family_relationship'].fillna(\n",
    "    students['family_relationship'].median())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.0    152\n",
       "4.0    110\n",
       "2.0     61\n",
       "5.0     37\n",
       "1.0     18\n",
       "NaN      9\n",
       "Name: freetime, dtype: int64"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['freetime'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "freetime\n",
       "1.0    50.0\n",
       "2.0    60.0\n",
       "3.0    50.0\n",
       "4.0    55.0\n",
       "5.0    60.0\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='freetime')['score'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['freetime'] = students['freetime'].fillna(3.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.0    126\n",
       "2.0     99\n",
       "4.0     81\n",
       "5.0     51\n",
       "1.0     23\n",
       "NaN      7\n",
       "Name: goout, dtype: int64"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['goout'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "goout\n",
       "1.0    55.0\n",
       "2.0    60.0\n",
       "3.0    55.0\n",
       "4.0    50.0\n",
       "5.0    50.0\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='goout')['score'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['goout'] = students['goout'].fillna(3.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.0    136\n",
       "3.0     88\n",
       "4.0     59\n",
       "1.0     47\n",
       "2.0     42\n",
       "NaN     15\n",
       "Name: health, dtype: int64"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['health'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['health'] = students['health'].fillna(5.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        6.0\n",
       "1        4.0\n",
       "2       10.0\n",
       "3        2.0\n",
       "4        4.0\n",
       "       ...  \n",
       "390    212.0\n",
       "391      3.0\n",
       "392      3.0\n",
       "393      0.0\n",
       "394      5.0\n",
       "Name: absences, Length: 387, dtype: float64"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['absences']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0      110\n",
       "2.0       60\n",
       "4.0       51\n",
       "6.0       30\n",
       "8.0       20\n",
       "10.0      17\n",
       "12.0      12\n",
       "NaN       11\n",
       "14.0      11\n",
       "16.0       7\n",
       "3.0        7\n",
       "7.0        6\n",
       "5.0        5\n",
       "18.0       5\n",
       "20.0       4\n",
       "1.0        3\n",
       "22.0       3\n",
       "9.0        3\n",
       "13.0       2\n",
       "15.0       2\n",
       "11.0       2\n",
       "25.0       1\n",
       "54.0       1\n",
       "385.0      1\n",
       "26.0       1\n",
       "56.0       1\n",
       "24.0       1\n",
       "212.0      1\n",
       "21.0       1\n",
       "75.0       1\n",
       "30.0       1\n",
       "19.0       1\n",
       "38.0       1\n",
       "40.0       1\n",
       "23.0       1\n",
       "17.0       1\n",
       "28.0       1\n",
       "Name: absences, dtype: int64"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['absences'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['absences'] = students['absences'].fillna(\n",
    "    students['absences'].median())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see a mistake value here so we delete it."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "students = students.loc[students['absences'] != 385.0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>school</th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>parents_status</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>mother_job</th>\n",
       "      <th>father_job</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>school_suppport</th>\n",
       "      <th>family_support</th>\n",
       "      <th>paid_additional_classes</th>\n",
       "      <th>additional_activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>higher_education</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>family_relationship</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>teacher</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>NaN</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>health</td>\n",
       "      <td>NaN</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GP</td>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  school sex  age address famsize parents_status  mother_education  \\\n",
       "0     GP   F   18       U     NaN              A               4.0   \n",
       "1     GP   F   17       U     GT3            NaN               1.0   \n",
       "2     GP   F   15       U     LE3              T               1.0   \n",
       "3     GP   F   15       U     GT3              T               4.0   \n",
       "4     GP   F   16       U     GT3              T               3.0   \n",
       "\n",
       "   father_education mother_job father_job  reason guardian  traveltime  \\\n",
       "0               4.0    at_home    teacher  course   mother         2.0   \n",
       "1               1.0    at_home      other  course   father         1.0   \n",
       "2               1.0    at_home      other   other   mother         1.0   \n",
       "3               2.0     health        NaN    home   mother         1.0   \n",
       "4               3.0      other      other    home   father         1.0   \n",
       "\n",
       "   studytime  failures school_suppport family_support paid_additional_classes  \\\n",
       "0        2.0       0.0             yes             no                      no   \n",
       "1        2.0       0.0              no            yes                      no   \n",
       "2        2.0       3.0             yes             no                     NaN   \n",
       "3        3.0       0.0              no            yes                     yes   \n",
       "4        2.0       0.0              no            yes                     yes   \n",
       "\n",
       "  additional_activities nursery higher_education internet romantic  \\\n",
       "0                    no     yes              yes      NaN       no   \n",
       "1                    no      no              yes      yes       no   \n",
       "2                    no     yes              yes      yes      NaN   \n",
       "3                   yes     yes              yes      yes      yes   \n",
       "4                    no     yes              yes       no       no   \n",
       "\n",
       "   family_relationship  freetime  goout  health  absences  score  \n",
       "0                  4.0       3.0    4.0     3.0       6.0   30.0  \n",
       "1                  5.0       3.0    3.0     3.0       4.0   30.0  \n",
       "2                  4.0       3.0    2.0     3.0      10.0   50.0  \n",
       "3                  3.0       2.0    2.0     5.0       2.0   75.0  \n",
       "4                  4.0       3.0    2.0     5.0       4.0   50.0  "
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Nominative variables"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After analysis we desided to delete column School, because this is a cathegorical data, that gives us nothing for analisys because we have no information about these schools (type, rating, etc.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "students.drop(['school'], inplace=True, axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Updating the list of columns with nominative variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['sex', 'address', 'famsize', 'parents_status', 'mother_job', 'father_job', 'reason', 'guardian', 'school_suppport', 'family_support', 'paid_additional_classes', 'additional_activities', 'nursery', 'higher_education', 'internet', 'romantic']\n"
     ]
    }
   ],
   "source": [
    "list_of_nominative = students.select_dtypes('object').columns.tolist()\n",
    "print(list_of_nominative)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Sex column has no null values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "U      288\n",
       "R       83\n",
       "NaN     15\n",
       "Name: address, dtype: int64"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['address'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0    10\n",
       "2.0     5\n",
       "Name: traveltime, dtype: int64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students[(students['address'] != 'U') & (\n",
    "    students['address'] != 'R')]['traveltime'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['address'] = students['address'].fillna('U')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GT3    252\n",
       "LE3    107\n",
       "NaN     27\n",
       "Name: famsize, dtype: int64"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['famsize'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['famsize'] = students['famsize'].fillna('GT3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "T      307\n",
       "NaN     43\n",
       "A       36\n",
       "Name: parents_status, dtype: int64"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['parents_status'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['parents_status'] = students['parents_status'].fillna('T')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "other       127\n",
       "services     95\n",
       "at_home      58\n",
       "teacher      55\n",
       "health       32\n",
       "NaN          19\n",
       "Name: mother_job, dtype: int64"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['mother_job'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['mother_job'] = students['mother_job'].fillna('other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mother_job\n",
       "at_home     45.689655\n",
       "health      60.625000\n",
       "other       50.273973\n",
       "services    54.526316\n",
       "teacher     55.181818\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='mother_job')['score'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "other       193\n",
       "services     98\n",
       "NaN          36\n",
       "teacher      28\n",
       "at_home      16\n",
       "health       15\n",
       "Name: father_job, dtype: int64"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['father_job'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['father_job'] = students['father_job'].fillna('other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "course        135\n",
       "reputation    101\n",
       "home          100\n",
       "other          33\n",
       "NaN            17\n",
       "Name: reason, dtype: int64"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['reason'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on the other value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['reason'] = students['reason'].fillna('other')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mother    247\n",
       "father     85\n",
       "NaN        30\n",
       "other      24\n",
       "Name: guardian, dtype: int64"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['guardian'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['guardian'] = students['guardian'].fillna('mother')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     330\n",
       "yes     48\n",
       "NaN      8\n",
       "Name: school_suppport, dtype: int64"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['school_suppport'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['school_suppport'] = students['school_suppport'].fillna('no')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "yes    214\n",
       "no     135\n",
       "NaN     37\n",
       "Name: family_support, dtype: int64"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['family_support'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['family_support'] = students['family_support'].fillna('yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     195\n",
       "yes    152\n",
       "NaN     39\n",
       "Name: paid_additional_classes, dtype: int64"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['paid_additional_classes'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We have a lot of missed values here so if we delete them we will loose a lot of data, so let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['paid_additional_classes'] = students['paid_additional_classes'].fillna(\n",
    "    'no')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "yes    191\n",
       "no     181\n",
       "NaN     14\n",
       "Name: additional_activities, dtype: int64"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['additional_activities'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['additional_activities'] = students['additional_activities'].fillna(\n",
    "    'yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "yes    295\n",
       "no      76\n",
       "NaN     15\n",
       "Name: nursery, dtype: int64"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['nursery'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['nursery'] = students['nursery'].fillna('yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "yes    348\n",
       "no      19\n",
       "NaN     19\n",
       "Name: higher_education, dtype: int64"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['higher_education'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['higher_education'] = students['higher_education'].fillna('yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "yes    297\n",
       "no      55\n",
       "NaN     34\n",
       "Name: internet, dtype: int64"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['internet'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['internet'] = students['internet'].fillna('yes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "no     232\n",
       "yes    123\n",
       "NaN     31\n",
       "Name: romantic, dtype: int64"
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students['romantic'].value_counts(dropna=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's fill null values on mode value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [],
   "source": [
    "students['romantic'] = students['romantic'].fillna('no')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 386 entries, 0 to 394\n",
      "Data columns (total 28 columns):\n",
      " #   Column                   Non-Null Count  Dtype  \n",
      "---  ------                   --------------  -----  \n",
      " 0   sex                      386 non-null    object \n",
      " 1   age                      386 non-null    int64  \n",
      " 2   address                  386 non-null    object \n",
      " 3   famsize                  386 non-null    object \n",
      " 4   parents_status           386 non-null    object \n",
      " 5   mother_education         386 non-null    float64\n",
      " 6   father_education         386 non-null    float64\n",
      " 7   mother_job               386 non-null    object \n",
      " 8   father_job               386 non-null    object \n",
      " 9   reason                   386 non-null    object \n",
      " 10  guardian                 386 non-null    object \n",
      " 11  traveltime               386 non-null    float64\n",
      " 12  studytime                386 non-null    float64\n",
      " 13  failures                 386 non-null    float64\n",
      " 14  school_suppport          386 non-null    object \n",
      " 15  family_support           386 non-null    object \n",
      " 16  paid_additional_classes  386 non-null    object \n",
      " 17  additional_activities    386 non-null    object \n",
      " 18  nursery                  386 non-null    object \n",
      " 19  higher_education         386 non-null    object \n",
      " 20  internet                 386 non-null    object \n",
      " 21  romantic                 386 non-null    object \n",
      " 22  family_relationship      386 non-null    float64\n",
      " 23  freetime                 386 non-null    float64\n",
      " 24  goout                    386 non-null    float64\n",
      " 25  health                   386 non-null    float64\n",
      " 26  absences                 386 non-null    float64\n",
      " 27  score                    386 non-null    float64\n",
      "dtypes: float64(11), int64(1), object(16)\n",
      "memory usage: 87.5+ KB\n"
     ]
    }
   ],
   "source": [
    "students.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAU0AAAEaCAYAAACVewWLAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAVcklEQVR4nO3debCldX3n8feHZrEB2VuEhha0Ebc4Ee64jEmmSzQiRhszrmMSNBBGy7Q9MRMlzLhMlWiYEBV7HB0CRtTEEYkWqIwWEg2VSsmk252AcgsBexFbaEAW2fzOH+e5yaW93X1/0Oc859x+v6pOnfPs33Pvrc/9/Z41VYUkaX5267sASZokhqYkNTA0JamBoSlJDQxNSWpgaEpSA0NTEyXJx5K8eyeu791JfprkxztrnVrYDE09LEluSHJPkjuTbEnyxSRH9l3XbEkqyfLtTD8S+GPgKVX12NFVpklmaOqReElV7QscBtwMrOm5nlaPA26pqp+0Lphk9yHUowlgaOoRq6qfAxcDT5kZl2T/JB9PsjnJjUn+W5LdumkfTnLxrHnPTnJFBlYkWZ/kzK7bfEOS125r20n+IMl0kluTXJrk8G78ld0s3+5aw6/aarnnA5cDh3fTP9aNf2mSq5PcluRrSZ48a5kbkrwtyXeAu7YOzq7+9yf5SZLbk3wnydO6aXslOSfJTUluTvKRJIu7aW9L8vWZ9SV5Y1fDoxp/FRqFqvLlq/kF3AA8v/u8N3Ah8PFZ0z8OXAI8GjgK+AFw6qz5fwC8Dvh14KfAEd20FcADwPuAvYB/D9wFHNtN/xjw7u7z87plj+vmXQNcOauGApZv5zusANbPGn5it60XAHsAbwWmgT1nfedvAUcCi+dY3wuBdcABQIAnA4d10z4AXAoc1P1MPg+8t5u2G3Al8C7gGGAL8Iy+f8e+tvF303cBvibz1QXIncBtXchtBH6lm7YIuJfBvsKZ+f8T8LVZw88EbgVuBF4za/xMaO4za9xFwNu7z7ND8wLgf8yab1/gfuCobrg1NN8OXDRreDdgA7Bi1nf+/e2s73ndP4NnA7vNGp8ujJ8wa9xzgB/OGj6q+3lcA/xp379fX9t+2T3XI3FyVR3AoJX3h8DfJ3kscAiwJ4NAnHEjsHRmoKr+H3A9g0C5aKv1bqmqu7Za9vA5tn/47G1U1Z3ALbO302jr9f0C+NFW6/vRthauqr8D/ifwIeDmJOcl2Q9YwqB1va7r9t8GfKkbP7PsDcBXGYTnhx5m/RoBQ1OPWFU9WFWfBR4Efo1Bl/l+BgdaZixj0GoDIMmbGITtRgbd4NkOTLLPVstunGPTG2dvo1vm4NnbabT1+sKgKz57fdu9LVhVfbCqjgeeyqC7/ycMfh73AE+tqgO61/41OIg2s62TGLQ+rwD+/GHWrxEwNPWIdQdAVgIHAtdU1YMMWo9nJXl0kscBbwE+2c3/RODdwO8Avwu8NcmvbrXa/55kzyS/DvwW8Jk5Nv03wOuT/GqSvYD3AFd1rTYYHNF/fMNXuQh4cZITkuzB4HSke4F/nM/CSf5tkmd1y94F/Bx4sGux/iXw/iSP6eZdmuSF3edDGOxqOA04BXhJF6IaQ4amHonPJ7kTuAM4Czilqq7upq1iEBzXA//AIOA+2h0h/iRwdlV9u6quA84EPtEFH8CPGRwM2Qj8NfCGqrp2641X1RUM9kP+LbAJeALw6lmzvAu4sOsSv3JHX6aqvs8gyNcwaB2+hMFpVffN8+exH4Nw3MKgm38LcE437W0MDip9PckdwFeAY7tp5wGXVNVlVXULcCpwfpKD57ldjVCqvAmxxkeSFcAnq+qIvmuR5mJLU5IaGJqS1MDuuSQ1sKUpSQ0MTUlqMNF3ajnkkEPqqKOO6rsMSQvMunXrflpVS+aaNtGhedRRR7F27dq+y5C0wCS5cVvT7J5LUgNDU5IaGJqS1MDQlKQGQwvNJB/tbvv/vVnjDkpyeZLruvcDu/FJ8sHusQXfSXLcsOqSpEdimC3NjwEnbjXuDOCKqjqGwX0Dz+jGv4jBbf6PAU4HPjzEuiTpYRtaaFbVlQxu3z/bSgbPkqF7P3nW+I/XwNeBA5IcNqzaJOnhGvV5modW1SaAqto0c0NWBo8TmP0YgfXduE0jrk/qzZo1a5ienh7Z9jZsGNyQfunSh/t0kHbLly9n1apVI9veMIzLye2ZY9ycdxJJcjqDLjzLli0bZk3SgnbPPff0XcJEGnVo3pzksK6VeRjwk278egbPYplxBHM/E4aqOo/Bna6ZmpryFk1aMEbdAlu9ejUA55577ki3O+lGfcrRpQyegUL3fsms8b/XHUV/NnD7TDdeksbJ0FqaST7F4LnShyRZD7wT+DPgoiSnAjcBr+hmvww4icEzVO4GXj+suiTpkRhaaFbVa7Yx6YQ55i3gTcOqRZJ2Fq8IkqQGhqYkNTA0JamBoSlJDcbl5PYFy6s8pIXF0FxgvMpDGi5Dc8i8ykNaWNynKUkNDE1JamBoSlIDQ1OSGhiaktTA0JSkBoamJDUwNCWpgaEpSQ0MTUlqYGhKUgNDU5IaGJqS1MDQlKQGhqYkNTA0JamBoSlJDQxNSWpgaEpSA0NTkhoYmpLUwNCUpAaGpiQ1MDQlqUEvoZnkj5JcneR7ST6V5FFJjk5yVZLrknw6yZ591CZJ2zPy0EyyFHgzMFVVTwMWAa8GzgbeX1XHAFuAU0ddmyTtSF/d892BxUl2B/YGNgHPAy7upl8InNxTbZK0TSMPzaraAJwD3MQgLG8H1gG3VdUD3WzrgaWjrk2SdqSP7vmBwErgaOBwYB/gRXPMWttY/vQka5Os3bx58/AKlaQ59NE9fz7ww6raXFX3A58F/h1wQNddBzgC2DjXwlV1XlVNVdXUkiVLRlOxJHX6CM2bgGcn2TtJgBOAfwa+Cry8m+cU4JIeapOk7epjn+ZVDA74fAP4blfDecDbgLckmQYOBi4YdW2StCO773iWna+q3gm8c6vR1wPP7KEcSZo3rwiSpAaGpiQ1MDQlqYGhKUkNDE1JamBoSlIDQ1OSGhiaktTA0JSkBoamJDUwNCWpgaEpSQ0MTUlq0MtdjqRJsWbNGqanp/suYyhmvtfq1at7rmR4li9fzqpVq3bqOg1NaTump6e57upvsmzfB/suZafb8/5BR/PeG9f2XMlw3HTnoqGs19CUdmDZvg9y5nF39F2GGr3nG/sNZb3u05SkBoamJDUwNCWpgaEpSQ0MTUlqYGhKUgNDU5Ia7HLnaS7kKzzAqzykYdvlQnN6eppvfe8aHtz7oL5LGYrd7isA1l1/c8+VDMeiu2/tuwTt4na50AR4cO+DuOdJJ/Vdhh6Gxdde1ncJ2sW5T1OSGhiaktTA0JSkBoamJDXoJTSTHJDk4iTXJrkmyXOSHJTk8iTXde8H9lGbJG1PXy3Nc4EvVdWTgH8DXAOcAVxRVccAV3TDkjRWRh6aSfYDfgO4AKCq7quq24CVwIXdbBcCJ4+6NknakT5amo8HNgN/leSbSc5Psg9waFVtAujeH9NDbZK0XX2E5u7AccCHq+oZwF00dMWTnJ5kbZK1mzdvHlaNkjSnPkJzPbC+qq7qhi9mEKI3JzkMoHv/yVwLV9V5VTVVVVNLliwZScGSNGPkoVlVPwZ+lOTYbtQJwD8DlwKndONOAS4ZdW2StCN9XXu+CvjrJHsC1wOvZxDgFyU5FbgJeEVPtUnSNvUSmlX1LWBqjkknjLoWSWrhFUGS1MDQlKQGhqYkNZh3aCb5tSSv7z4vSXL08MqSpPE0rwNBSd7J4MDNscBfAXsAnwSeO7zShmPDhg0suvt27wA+oRbdfQsbNjwwsu1t2LCBu362iPd8Y7+RbVM7x40/W8Q+Gzbs9PXOt6X5MuClDK7eoao2Ao/e6dVI0pib7ylH91VVJSmA7lrxibR06VJ+fO/uPiNoQi2+9jKWLj10ZNtbunQp9z6wiTOPu2Nk29TO8Z5v7MdeS5fu9PXOt6V5UZL/DRyQ5A+ArwB/udOrkaQxN6+WZlWdk+QFwB0M9mu+o6ouH2plkjSGdhiaSRYBX66q5wMGpaRd2g6751X1IHB3kv1HUI8kjbX5Hgj6OfDdJJfTHUEHqKo3D6UqSRpT8w3NL3YvSdqlzfdA0IXdbdye2I36flXdP7yyJGk8zfeKoBUMHnZ2AxDgyCSnVNWVwytNksbPfLvnfwH8ZlV9HyDJE4FPAccPqzBJGkfzPbl9j5nABKiqHzC4/lySdinzbWmuTXIB8Ilu+LXAuuGUJEnja76h+UbgTcCbGezTvBL4X8MqSpLG1XxDc3fg3Kp6H/zLVUJ7Da0qSRpT892neQWweNbwYgY37ZCkXcp8Q/NRVXXnzED3ee/hlCRJ42u+oXlXkuNmBpJMAfcMpyRJGl/z3ae5GvhMko1AAYcDrxpaVZI0puYbmkcDzwCWMXj0xbMZhKe04N1058J8RtDNdw86mofu/YueKxmOm+5cxDFDWO98Q/PtVfWZJAcAL2BwhdCHgWcNoSZpbCxfvrzvEobmvulpAPZ63ML8jscwnN/ffEPzwe79xcBHquqSJO/a6dVIY2bVqlV9lzA0q1evBuDcc8/tuZLJMt8DQRu6ZwS9ErgsyV4Ny0rSgjHf4Hsl8GXgxKq6DTgI+JOhVSVJY2q+99O8G/jsrOFNwKZhFSVJ48outiQ16C00kyxK8s0kX+iGj05yVZLrkny6u1O8JI2VPluaq4FrZg2fDby/qo4BtgCn9lKVJG1HL6GZ5AgGpy+d3w0HeB5wcTfLhcDJfdQmSdsz3/M0d7YPAG8FHt0NHwzcVlUPdMPrgaXD2viiu29l8bWXDWv1vdrt53cA8ItHLbwrWGDwu4ND+y5Du7CRh2aS3wJ+UlXruge2weDGxlub8zLNJKcDpwMsW7asefsL+QoPgOnpnwGw/PELNVgOXfC/Q423PlqazwVemuQk4FHAfgxangck2b1rbR4BbJxr4ao6DzgPYGpqqvn694V8hQd4lYc0bCPfp1lVf1pVR1TVUcCrgb+rqtcCXwVe3s12CnDJqGuTpB0Zp/M03wa8Jck0g32cF/RcjyT9kr4OBAFQVV8DvtZ9vh54Zp/1SNKOjFNLU5LGnqEpSQ0MTUlqYGhKUgNDU5IaGJqS1MDQlKQGhqYkNTA0JamBoSlJDQxNSWpgaEpSA0NTkhoYmpLUwNCUpAaGpiQ1MDQlqYGhKUkNDE1JamBoSlIDQ1OSGhiaktTA0JSkBr0+91zSv1qzZg3T09Mj297MtlavXj2ybS5fvpxVq1aNbHvDYGhKu6jFixf3XcJEMjSlMTHpLbBdhfs0JamBoSlJDQxNSWpgaEpSg5GHZpIjk3w1yTVJrk6yuht/UJLLk1zXvR846tokaUf6aGk+APxxVT0ZeDbwpiRPAc4ArqiqY4ArumFJGisjD82q2lRV3+g+/wy4BlgKrAQu7Ga7EDh51LVJ0o70ep5mkqOAZwBXAYdW1SYYBGuSx/RY2k7jVR7SwtJbaCbZF/hb4D9X1R1J5rvc6cDpAMuWLRtegRPKqzyk4UpVjX6jyR7AF4AvV9X7unHfB1Z0rczDgK9V1bHbW8/U1FStXbt2+AVL2qUkWVdVU3NN6+PoeYALgGtmArNzKXBK9/kU4JJR1yZJO9JH9/y5wO8C303yrW7cmcCfARclORW4CXhFD7VJ0naNPDSr6h+Abe3APGGUtUhSK68IkqQGhqYkNTA0JamBoSlJDQxNSWpgaEpSA0NTkhoYmpLUwNCUpAaGpiQ1MDQlqYGhKUkNDE1JamBoSlIDQ1OSGhiaktTA0JSkBoamJDUwNCWpgaEpSQ0MTUlqYGhKUgNDU5IaGJqS1MDQlKQGhqYkNTA0JamBoSlJDQxNSWpgaEpSA0NTkhqMVWgmOTHJ95NMJzmj73om0cqVK1mxYgUve9nL+i5FY+60005jxYoVvOENb+i7lIkyNqGZZBHwIeBFwFOA1yR5Sr9VTZ7bb78dgC1btvRcicbd9PQ0ANdee23PlUyWsQlN4JnAdFVdX1X3Af8HWNlzTRNl5cqH/rhsbWpbTjvttIcM29qcv3EKzaXAj2YNr+/GaZ5mWpkzbG1qW2ZamTNsbc7fOIVm5hhXvzRTcnqStUnWbt68eQRlSdK/GqfQXA8cOWv4CGDj1jNV1XlVNVVVU0uWLBlZcZIE4xWa/wQck+ToJHsCrwYu7bmmibL//vs/ZPjAAw/sqRKNu+XLlz9k+ElPelJPlUyesQnNqnoA+EPgy8A1wEVVdXW/VU2WSy655CHDn/vc53qqROPu/PPPf8jwRz7ykZ4qmTxjE5oAVXVZVT2xqp5QVWf1Xc8kmmlt2srUjsy0Nm1ltknVLx1rmRhTU1O1du3avsuQtMAkWVdVU3NNG6uWpiSNO0NTkhoYmpLUwNCUpAYTfSAoyWbgxr7rGEOHAD/tuwhNBP9W5va4qprz6pmJDk3NLcnabR35k2bzb6Wd3XNJamBoSlIDQ3NhOq/vAjQx/Ftp5D5NSWpgS1OSGhiaC0SSx/ZdgyZHEu/o8jAZmgtAkhcDlybxrszaoSS/CVzevauRoTnhkpwInAG8o6o2J9mj75o09o4Fngb8lyQn913MpNm97wL08CU5CLgM+O2q+lKSJwDvSPJHwJbyKJ/m9ing8cBNwO8l2aOqPtNzTRPDluYEq6pbgZcwCMqnMzh95JtVdauBqdmSPL37GwG4FbgPeCrwYeB3kvyH3oqbMIbmhKuqLwJnAt8CLq+qDyTZLclcT/fULijJwQz+Pr6Q5OXA8cB/Be5lkAF/w6DF+Zr+qpwchuYCUFVfAl4IvC7J/lX1C2BRz2VpTFTVLcDzGTzh9enAicDHgbuBJVX1aeBzwMokj+6t0Anhye0LSJIXAR8AntN13aV/keQE4KPAccDLgf/I4NHZrwf2Aqiqn/VW4IQwNBeYJCuBdwJTQLlvU7MlOQk4m8E/1juTHF1VP+y7rkliaC5ASfatqjv7rkPjqQvOvwCeO9MjSRL/wc6PpxwtQAamtqeqLuvO5/1KEnskjWxpSrsoeyQPj6EpSQ085UiSGhiaktTA0JSkBoamJDUwNCWpgaEpSQ0MTS0YSfZJ8sUk307yvSSvSnJ8kr9Psi7Jl5MclmT3JP+UZEW33HuTnNVz+ZoQXhGkheREYGNVvRggyf7A/wVWdne1fxVwVlX9fpLXARcneXO33LP6KlqTxdDUQvJd4JwkZwNfALYweKzD5d3tRRcBmwCq6uoknwA+z+DmFff1U7ImjaGpBaOqfpDkeOAk4L3A5cDVVfWcbSzyK8BtwKEjKlELgPs0tWAkORy4u6o+CZzDoMu9JMlzuul7JHlq9/m3gYOB3wA+mOSAnsrWhPHacy0YSV4I/DnwC+B+4I3AA8AHgf0Z9Kw+wOAu5f8InFBVP+r2ax5fVaf0UrgmiqEpSQ3snktSA0NTkhoYmpLUwNCUpAaGpiQ1MDQlqYGhKUkNDE1JavD/AfOp5CNTnR1uAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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mpllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZWh6aEraT9KNkpZKulvS7DR+oqTrJd2Xfk5odm1mZttTRU/zWeDMiPgd4HDgdEmHAGcDN0TENOCGNGxm1lKaHpoRsSYibkvPnwSWAt3AccDC1GwhcHyzazMz255Kj2lK6gFeA9wMTI6INVAEK/CS6iozM6utstCUtAfwPeDDEfFExnwzJS2RtGTdunWNK9DMrIZKQlPSrhSBeXlEXJlGr5U0JU2fAjxUa96ImB8RfRHRN2nSpOYUbGaWVPHpuYCLgKURcX5p0tXAjPR8BnBVs2szM9ueKu5GeSRwMnCnpDvSuHOAzwKLJJ0GrADeVUFtZmbDanpoRsSPAQ0x+ahm1mJmlstnBJmZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZWip0JT0Vkm/lNQv6eyq62lH/f39HHvssfT391ddillHapnQlNQFfBl4G3AIcKKkQ6qtqv3MnTuXjRs3Mnfu3KpLMetILROawGFAf0Qsi4hngG8Dx1VcU1vp7+9n+fLlACxfvty9TbMGGFV1ASXdwIOl4ZXA6yqqpS0N7l3OnTuXBQsWVFOMZZs3b15T/9ENrGv27NlNW2dvby+zZs1q2voaoZVCUzXGxQsaSTOBmQBTp05tdE1tZaCXOdSwWdmYMWOqLqEttVJorgT2Kw3vC6we3Cgi5gPzAfr6+l4QqiNZT0/PNkHZ09NTWS2Wr917YCNFKx3TvAWYJukASaOB9wJXV1xTWzn33HOHHTaz317LhGZEPAt8CLgOWAosioi7q62qvfT29j7fu+zp6aG3t7fagsw6UMuEJkBEXBsRB0XEyyLi76qupx2de+65jBs3zr1MswZppWOathP09vZyzTXXVF2GWcdqqZ6mmVmrc2iamWVwaJqZZVBE+37VUdI64IGq62hBewMPV12EtQX/rtS2f0RMqjWhrUPTapO0JCL6qq7DWp9/V/J599zMLIND08wsg0OzM82vugBrG/5dyeRjmmZmGdzTNDPL4NA0G4Ek+WK0O8ihaTbCSDoGuEFSd9W1tCOHZgeQNHnQsN9Xq0nSHwNfAE6OiFX+XcnnDdbmJB0MrJF0vqQPAETEc2ma3197nqQ/Ai4B7gEeheJ3RVKtW83YEPxH1f42Av8NrAVOkLRQ0tsl7TUQnmaSjgL+GfgI8FPg/ZJeDxAR4eCsn0OzzUXEg8DPgUOBY4F/B04DrpF0mKRpVdZnLeMJ4JSIuBy4BtgCHCvpSHBw5vD3NNuYJKVf9tEUu10fBg4GLgZ+CLwUWAN8NCI2VleptQpJu6Rd8mnAycCuwPcj4qcVl9Y2HJptLvUORgOfBA6k6HGeHRH/mv4wHo6Ix6qs0VpT+v34M+DFwOURcXPFJbUFh2aHkPRy4L+AeRHx/6uux9pD+iDxncDXI2Jd1fW0A4dmB5F0KrA/8PmI2FR1PdYeJO0aEVuqrqNd+IOgzvLfwGurLsLaiwMzj3uaHUbSWPcyzRrHoWlmlsG752ZmGRyaZmYZHJpmZhkcmtYxJI2X9Nc7cXmnSNpnZ7WzzuDQtJYkadQOzDYe2GmhCZwC1BOG9bazDuDQtIaR1CPp3nTlpV9IukLSWEmfknSLpLskzR+4UISkxZLOk/QjYLakSZK+l9reMnBxCUlzJF2c2i+TdEZa5WeBl0m6Q9I/SJoi6aY0fJekNwxRZ5ekBanNnZL+RtIJQB9weZp/TK26h2i3XNLeadl9khan53+Y2twh6XZJezZy+1uDRIQffjTkAfQAARyZhi8GPgpMLLW5FHh7er4Y+Epp2jeB16fnU4Gl6fkcisub7QbsDTxCceGJHuCu0vxnAn+bnncBew5R52uB60vD40v19JXGD1d3ud1yYO/0vA9YnJ5/v7Qt9gBGVf0e+ZH/2JFdILMcD0bET9Lzy4AzgPslnQWMBSYCd1MECsB3SvMeDRxSumLZXqXe2TUR8TTwtKSHgG2uXp/cAlwsaVfgXyPijiFqXAYcKGkexWXTfjhEuzcNU3c9fgKcL+ly4MqIWJkxr7UI755bow0+eyKArwAnRMQrga8Bu5emly9htwtwRES8Oj26I+LJNO3pUrut8MIOQETcBLwRWAVcKul9NQssrgL1exQ9xtOBrw9uI2n37dRd9iy/+dt6vk1EfBb4C2AM8LN0sQxrMw5Na7Spko5Iz08EfpyePyxpD+CEYeb9IfChgQFJr97Oup4Enj9OKGl/4KGI+BpwEcVl814gHX/cJSK+R3GJvYF25eUNhF+turdZL8Xu+cA1AP60tJ6XRcSdEfE5YAnFtU+tzXj33BptKTBD0r8A9wEXAhOAOynC5ZZh5j0D+LKkX1D8rt4EfHCoxhHxiKSfSLoL+DfgLuBjkrYAG4CaPU2gG/hG6Z5Kn0g/FwBflbQZOIKid1mr7sHtPgNcJOkcoHyNyg9LehNFz/ieVKO1GZ97bg0jqQf4QUS8ouJSzHYa756bmWVwT9NGFEk3U3xVqezkiLizinqs/Tg0zcwyePfczCyDQ9PMLIND08wsg0PTzCyDQ9PMLIND08wsw/8Bb48B7h37ZxMAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAU0AAAEhCAYAAAD7xvLlAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAa/UlEQVR4nO3df7xVdZ3v8debgwj+BBEdOYhYYKNNpXZybLLiBhZZN2lGU6+30PHGtQzot45p2uS1bPpFzIxeGkvMxh85zegjvTRKog+nSQX8gUrqiQHkQIqgCIg/gM/9Y32Pbo/nx/7q2XvtfXg/H4/9OHt/16/P2vuc9/mutfZaSxGBmZlVZ1DZBZiZNROHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6Z1S9IVki7qx/ldJOkpSX/sr3lmLn+cpJA0uAbzDknj+3u+1pgcmg1O0gpJWyVtlvS0pJskHVh2XZX6Co1U75eAwyLiT+pXmfUnSRdKuqrsOsrm0GwO/z0i9gAOAJ4A5pRcT66DgPUR8WTuhLXoGVo+fw6vcGg2kYh4HrgeOKyzTdLekq6UtE7SSknnSRqUhl0q6fqKcS+RtECFiZJWSzo3bTavkHRqT8uW9GlJ7ZI2SLpR0ujUfkca5f7UGz6py3STgVuA0Wn4Fan9Y5IekvSMpIWSDq2YZoWksyU9AGzp+geb6v+BpCclbZT0gKQ/S8OGSfpeei82SrpT0rCKyU+VtCqt89cq5rmrpB9KWpMeP5S0a1/rXy1Jx0l6WNImSR2SvpzaT5N0Z5dxX+65p90kl0m6JU17u6SDuow7U9LytE5/V/H5nybpPyTNSe/F7yVNqph2dFqXDWndPl0x7EJJ10u6StKzwJnAucBJ6XO8P2f9B5SI8KOBH8AKYHJ6vhswD7iyYviVwA3AnsA44FHgjIrxHwVOA94LPAWMScMmAtuA7wO7Au8HtgBvScOvAC5Kzz+Qpj0yjTsHuKOihgDG97IOE4HVFa8PScs6FtgF+CrQDgypWOf7gAOBYd3M70PAYmA4IOBQ4IA07B+AhUAr0AL8Rap5XKrzx8Aw4B3AC8Chabq/BX4H7AeMAn4LfLM/1j+NsxZ4b3o+AjgyPT8NuLPLuC/PL30Om4D3pWXPrhw/jXsbsA8wNn3e/6ti3tuAL6T3+SRgI7BPGn478I/AUOBwYB0wKQ27EHgJmErRuRqW2q4q+2+i7EfpBfjRxwdUBMhm4Jn0B7AGeFsa1pL+8A+rGP9/AwsrXh8FbABWAqdUtE9M89u9ou064Pz0/ApeCc3Lge9UjLdH+oMal17nhub5wHUVrwcBHcDEinX+617m94EUDkcDg7rMZyvwjm6mGZfqHFPRdjdwcnr+B+C4imEfAlb0x/qncValz2avLu2n0XdoXtNl2duBAyvGnVIx/LPAgop5rwHUZZ0/SfEPaTuwZ8WwbwFXpOcXUvGPoaJtpw9Nb543h6kRMZyip/E54HZJfwLsCwyhCMROKyl6WQBExN3Acooe2XVd5vt0RGzpMm13m52jK5cREZuB9ZXLydR1fjuAx7vM7/GeJo6I3wB/T9GrfELSXEl7UbwfQykCsCeVR++fowih19TEq9+L/lj/vwKOA1amTex3Z0z78nuRlr2BV39Ole9V18+wI1LidRk+GtgQEZu6DKvqM9iZOTSbSERsj4hfUvQQjqHYZHyJ4kBLp7EUvTYAJJ1FEbZrKDaDK42QtHuXadd0s+g1lctI04ysXE6mrvMTRc+ncn69Xn4rIn4UEe8E3kqxuf8VivfjeeDNb7QmXv1evOH1j4h7IuJ4is3/f+OVf2BbKHajdM67u28XHFgxfA+KTfE13Q3ntZ9ha3p/uw5fA+wjac8uw3r7DHxJNByaTSUdADmeYp/YsojYTvHH938k7ZkOEHwRuCqNfwhwEfA/KTbJvirp8C6z/YakIZLeC3wU+EU3i/5n4HRJh6eDIxcDd0XEijT8CeBNGatyHfARSZMk7ULxdaQXKPYj9knSuyT9eZp2C0VQbk891p8A308HOVokvbvygE4vrgbOkzRK0r7A10nvI32vf1/1DpF0qqS9I+Il4FmKf3wA9wNvTfMeSrEJ3NVxko6RNAT4Zlp2ZS/wK5JGqPhq1yzg2oph+wEzJe0i6USK/b83p+l/C3xL0lBJbwfOAH7ey6o8AYzrPNC00yp7/4AfvT8o9u9tpdivuQl4EDi1YvgIij/udRSbU1+n+Gc4mGL/1TkV434GWErR85wIrAa+RtFDWwV8smLcK0j7NNPrMyk2ezcAv+LV+wbPpDjQ8QzwiW7WYSIV+zRT28eBhykOTNwOvLXLOk/u5T2ZBDyQ3pOnKP7Q90jDhgE/pOgxbQTuSG3jKHpKgyvms5BXDpoMBX6U1mNtej60yvXva5/uEGA+8DRFYN4DHFMxvPMzeJziH1zXfZqXUXwDYXNan4O7LHsmxS6Y9cD3gJY07DTgPyh2ZWyk2A/8wYppx6R12ZDW7cyKYRfSZf8lRe/6zrQeS8r+2yjrofRm2E5G0kSKP4oxZddiPVPxFa3VEXFeD8MDmBAR7d0MO43in8IxNS1yJ7Nzd7PNzDI5NM36iYov62/u5tHjSQPWfLx5bmaWwT1NM7MMDk0zswxNfeWSfffdN8aNG1d2GWY2wCxevPipiBjV3bCmDs1x48axaNGissswswFG0sqehnnz3Mwsg0PTzCyDQ9PMLIND08wsQ81CU9JPVNyO4MGKtn3SZfsfSz9HpHZJ+lG65P4Dko6sVV1mZm9ELXuaVwBTurSdQ3FV6QnAgvQa4MPAhPSYDlxaw7rMzF63moVmRNxBccmpSsdT3OOG9HNqRfuVUfgdMFzSAbWqzczs9ar39zT3j4i1ABGxVtJ+qb2VV19af3VqW1vn+sxKM2fOHNrbX3OFt5rp6Cgu0t7a+nrvWpJv/PjxzJgxo27Lq4VG+XK7umnr9koikqZTbMIzduzYWtZkNqBt3bq17BKaUr1D8wlJB6Re5gHAk6l9Na++z8kYur9XDRExF5gL0NbW5ks02YBR7x7YrFmzAJg9e3Zdl9vs6v2VoxuBaen5NIr7dXe2fyodRT8a2Ni5GW9m1khq1tOUdDXFvWH2lbQauAD4NnCdpDMo7klzYhr9Zorbm7ZT3Fb19FrVZWb2RtQsNCPilB4GTepm3ADOqlUtZmb9xWcEmZllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllcGiamWVwaJqZZXBompllKCU0JX1B0kOSHpR0taShkg6WdJekxyRdK2lIGbWZmfWm7qEpqRWYCbRFxJ8BLcDJwCXADyJiAvA0cEa9azMz60tZm+eDgWGSBgO7AWuBDwDXp+HzgKkl1WZm1qO6h2ZEdADfBVZRhOVGYDHwTERsS6OtBlrrXZuZWV/K2DwfARwPHAyMBnYHPtzNqNHD9NMlLZK0aN26dbUr1MysG2Vsnk8G/isi1kXES8Avgb8AhqfNdYAxwJruJo6IuRHRFhFto0aNqk/FZmZJGaG5Cjha0m6SBEwCHgZuA05I40wDbiihNjOzXpWxT/MuigM+S4ClqYa5wNnAFyW1AyOBy+tdm5lZXwb3PUr/i4gLgAu6NC8HjiqhHDOzqvmMIDOzDA5NM7MMDk0zswyl7NPcmcyZM4f29va6La+jowOA1tb6nRswfvx4ZsyYUbflmZXJoTnAbN26tewSzAY0h2aN1bsHNmvWLABmz55d1+Wa7Sy8T9PMLIND08wsg0PTzCyDQ9PMLIND08wsg0PTzCyDQ9PMLIO/p2nWi3qf0VVPnevV+d3egagWZ6s5NM160d7ezmMP3cvYPbaXXUq/G/JSsaH5wspFJVdSG6s2t9Rkvg5Nsz6M3WM75x75bNllWKaLl+xVk/l6n6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZhlJCU9JwSddL+r2kZZLeLWkfSbdIeiz9HFFGbWZmvSmrpzkbmB8Rfwq8A1gGnAMsiIgJwIL02sysodQ9NCXtBbwPuBwgIl6MiGeA44F5abR5wNR612Zm1pcyeppvAtYBP5V0r6R/krQ7sH9ErAVIP/croTYzs16VEZqDgSOBSyPiCGALGZvikqZLWiRp0bp162pVo5lZt8oIzdXA6oi4K72+niJEn5B0AED6+WR3E0fE3Ihoi4i2UaNG1aVgM7NOdQ/NiPgj8Likt6SmScDDwI3AtNQ2Dbih3rWZmfWlrLtRzgB+LmkIsBw4nSLAr5N0BrAKOLGk2szMelRKaEbEfUBbN4Mm1bsWM7McPiPIzCyDQ9PMLIND08wsQ9WhKekYSaen56MkHVy7sszMGlNVB4IkXUBx4OYtwE+BXYCrgPfUrrTamDNnDu3t7WWXUTOd6zZr1qySK6md8ePHM2PGjLosq6Ojgy2bWrh4yV51WZ71n5WbWti9o6Pf51vt0fOPA0cASwAiYo2kPfu9mjpob2/nvgeXsX23fcoupSYGvRgALF7+RMmV1EbLcxvKLsF2ctWG5osREZICIJ0r3rS277YPW//0uLLLsNdh2O9vruvyWltbeWHbWs498tm6LtfeuIuX7MWura39Pt9q92leJ+n/AsMlfRq4Ffhxv1djZtbgquppRsR3JR0LPEuxX/PrEXFLTSszM2tAfYampBbg1xExGXBQmtlOrc/N84jYDjwnae861GNm1tCqPRD0PLBU0i0U178EICJm1qQqM7MGVW1o3pQeZmY7tWoPBM1Ll3E7JDU9EhEv1a4sM7PGVO0ZQRMpbna2AhBwoKRpEXFH7UqrjY6ODlqe21j37/tZ/2h5bj0dHdvKLsN2YtVunn8P+GBEPAIg6RDgauCdtSrMzKwRVRuau3QGJkBEPCpplxrVVFOtra388YXBPiOoSQ37/c20tu5fdhm2E6s2NBdJuhz4WXp9KrC4NiWZmTWuakPzM8BZwEyKfZp3AP9Yq6LMzBpVtaE5GJgdEd+Hl88S2rVmVZmZNahqL9ixABhW8XoYxUU7zMx2KtWG5tCI2Nz5Ij3frTYlmZk1rmpDc4ukIztfSGoDttamJDOzxlXtPs1ZwC8krQECGA2cVLOqzMwaVLWheTDF7S7GUtz64miK8DQb8FZtHpj3CHriuWJDc//ddpRcSW2s2tzChBrMt9rQPD8ifiFpOHAsxRlClwJ/XoOazBrG+PHjyy6hZl5MN+Hb9aCBuY4TqM3nV21obk8/PwJcFhE3SLqw36sxazD1uutlGTrvWDp79uySK2ku1R4I6kj3CPoEcLOkXTOmNTMbMKoNvk8AvwamRMQzwD7AV2pWlZlZg6r2eprPAb+seL0WWFuroszMGpU3sc3MMpQWmpJaJN0r6Vfp9cGS7pL0mKRr05XizcwaSpk9zVnAsorXlwA/iIgJwNPAGaVUZWbWi1JCU9IYiq8v/VN6LeADwPVplHnA1DJqMzPrTbXf0+xvPwS+CuyZXo8EnomIzpu/rAZaa7Xwluc2DNh7BA16/lkAdgwdeGewQPHZga/cbuWpe2hK+ijwZEQsTjdsg+LCxl11e5qmpOnAdICxY8dmL38gn+EB0N6+CYDxbxqowbL/gP8MrbGV0dN8D/AxSccBQ4G9KHqewyUNTr3NMcCa7iaOiLnAXIC2trbs898H8hke4LM8zGqt7vs0I+JvImJMRIwDTgZ+ExGnArcBJ6TRpgE31Ls2M7O+NNL3NM8GviipnWIf5+Ul12Nm9hplHQgCICIWAgvT8+XAUWXWY2bWl0bqaZqZNTyHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZBoemmVkGh6aZWQaHpplZhlLve74zmDNnDu3t7XVbXueyZs2aVbdljh8/nhkzZtRteWZlcmgOMMOGDSu7BLMBzaFZY+6BmQ0s3qdpZpbBoWlmlsGhaWaWwaFpZpah7qEp6UBJt0laJukhSbNS+z6SbpH0WPo5ot61mZn1pYye5jbgSxFxKHA0cJakw4BzgAURMQFYkF6bmTWUuodmRKyNiCXp+SZgGdAKHA/MS6PNA6bWuzYzs76U+j1NSeOAI4C7gP0jYi0UwSppvxJLM6s7nz3WHEoLTUl7AP8CfD4inpVU7XTTgekAY8eOrV2BZgOczx57fRQR9V+otAvwK+DXEfH91PYIMDH1Mg8AFkbEW3qbT1tbWyxatKj2BZvZTkXS4oho625YGUfPBVwOLOsMzORGYFp6Pg24od61mZn1pYzN8/cAnwSWSrovtZ0LfBu4TtIZwCrgxBJqMzPrVd1DMyLuBHragTmpnrWYmeXyGUFmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkcmmZmGRyaZmYZHJpmZhkaKjQlTZH0iKR2SeeUXU8zWr9+PTNnzmT9+vVll2INbuLEiS8/rHoNE5qSWoB/AD4MHAacIumwcqtqPvPmzWPp0qVceeWVZZdiNiA1TGgCRwHtEbE8Il4ErgGOL7mmprJ+/Xrmz59PRDB//nz3Nq1HXXuX7m1Wr5FCsxV4vOL16tRmVZo3bx47duwAYPv27e5tmtVAI4WmummL14wkTZe0SNKidevW1aGs5nHrrbeybds2ALZt28Ytt9xSckVmA08jheZq4MCK12OANV1Hioi5EdEWEW2jRo2qW3HNYPLkyQwePBiAwYMHc+yxx5ZckdnA00iheQ8wQdLBkoYAJwM3llxTU5k2bRqDBhUfaUtLC5/61KdKrshs4GmY0IyIbcDngF8Dy4DrIuKhcqtqLiNHjmTKlClIYsqUKYwcObLskqxBLVy4sNfX1rPBZRdQKSJuBm4uu45mNm3aNFasWOFeplmNKOI1x1qaRltbWyxatKjsMsxsgJG0OCLauhvWMJvnZmbNwKFpZpbBoWlmlsGhaWaWoakPBElaB6wsu44GtC/wVNlFWFPw70r3DoqIbs+eaerQtO5JWtTTkT+zSv5dyefNczOzDA5NM7MMDs2BaW7ZBVjT8O9KJu/TNDPL4J6mmVkGh6aZWQaHpplZBofmACbpAEm7lV2HNQ9JzoQ++A0aoCR9DLgU35zOeiHpVEnnSZolaWxE7HBw9s5vzgAk6b3AN4CvR8RjkoZK2isN6+4GdrYTknQWMAPYBBwE/Iuk8RGxo9zKGltDXbnd3hhJiuI7ZIcCtwPbJX0WmAI8L+krEeFz9XdyFb8nbwNmRsTdqf1s4HxJZ0bE1lKLbGDuaQ4se6af9wDDgF9Q3Ab5cuC/gOEl1WWNZYKkXSju+Dqxov3/AS86MHvnnuYAIekjwCmSlgOLgXOAQRGxXtIRwLeBfy6zRiufpM8Bnwf+FbgfmCnpqYj4CUXP882S9o6IjWXW2cgcmgOApHcB3wGmUvQqxwHzi0E6Bvgp8IWIuL+0Iq106eDg24EPAR8E9gJuBS5K/1j/G3CSA7N3Po2yyUkaSxGWT1JcW3Q2cGJErJTUSnG9xF0iwneg24ml34X/BG6NiL+WtCvwV8CBwAiKc9A3RsT6EstsCt6n2cQk7U9xr/ingOkUv/gfT4F5AvBZYJkD0yKig2KzfIqkkyPiBeAaYB2wA9jgwKyON8+b21PAIcCbgEeAfwf2kjQaOB84LyJeLLE+ayAR8UtJLwDfkkREXCPpCmD3iNhUcnlNw5vnTSiF4h4R8WjaPP8y8CgwkmK/1GbgxxFxQ8XXS8wAkPRhiq2SL0TE9WXX02wcmk1G0u7ARcA7KDav/pNiM/xnEfFbSXtS7MPc4MC0nkg6FvhDRCwvu5Zm49BsQpKGAocBZwMPUOyrWgH8ZUQ8XmJpZgOe92k2oYh4HlgiaTqwK8UBvcMpvqz8uHuYZrXjnuYAIelrFLcdnV52LWYDmb9y1OQqLsDxB+AgScPKrMdsoHNoNrmIiBScW4Av+bxhs9ry5rmZWQb3NM3MMjg0zcwyODTNzDI4NM3MMjg0ra4knSbp7/tpXisk7dsf8yqDpKmSDiu7Dsvj0DQrgaTBFNdBdWg2GYem9QtJu0u6SdL9kh6UdJKkd0n6bWq7O11MBGC0pPmSHpP0nYp5nCJpaZr+kr7ac+tJ7S/3TiW1SVqYnl8o6WeSfpPq+nRqnyjpDkn/KulhSZd13uJW0mZJ35O0RNICSaNS++GSfifpgTTdiNS+UNLFkm6nuG7Ax4C/k3SfpDe/oQ/A6sbnnlt/mQKsiYiPAEjaG7iX4vYJ96RbCHd+8f5w4AjgBeARSXOA7cAlwDuBp4F/lzQVuLu79oj4t9dRT1/eDhwN7A7cK+mm1H4URY9wJcVtRP4SuD6NtyQiviTp68AFFBeFvhKYERG3S/rb1P75NK/hEfH+VNME4Fe+PFtzcU/T+stSYLKkS1Tcd30ssDYi7gGIiGcjYlsad0FEbEwXHnmY4p7b7wIWRsS6NN7Pgff10p5VT5X3vbkhIrZGxFPAbRRhCXB3RCyPiO3A1cAxqX0HcG16fhVwTArn4RFxe2qf16Xea7Gm5tC0fhERj1L0BpcC3wI+TnH74O68UPF8O8UWj3oYt6f2rHpSTxBgG6/83g/tOlkPr3tqf81iqyhtSxXjWANzaFq/SFeTfy4irgK+S7GZOzrdKRNJe6aDHz25C3i/pH0ltQCnALf30p5bz5Fp0AqKMIXixmKVjpc0VNJIivuB35Paj5J0cNqXeRJwZ2ofBJyQnv8P4M7Uo3069bYBPtlLvZt45V711iS8T9P6y9soDmrsAF4CPkPRS5yTrry0FZjc08QRsVbS31BsFgu4OSJuAOip/XXUA/AN4HJJ51IEcqW7gZsodi18MyLWSDqE4ur4307zvIPinuFQ9BrfKmkxsJEiUAGmAZdJ2g1YDpzeQ43XAD+WNBM4ISL+UMV6Wcl8wQ4ziqPnwOaI+G6X9onAlyPio91Mszki9qhPhdYovHluZpbBPU1ramn/44JuBk3yfbytFhyaZmYZvHluZpbBoWlmlsGhaWaWwaFpZpbBoWlmluH/A+bUQxewxug2AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def get_boxplot(column):  # Function to show outliers in boxplot\n",
    "    fig, ax = plt.subplots(figsize=(5, 4))\n",
    "    sns.boxplot(x=column, y='score',\n",
    "                data=students.loc[students.loc[:, column].isin(\n",
    "                    students.loc[:, column].value_counts().index[:])],\n",
    "                ax=ax)\n",
    "    plt.xticks(rotation=45)\n",
    "    ax.set_title('Boxplot for ' + column)\n",
    "    plt.show()\n",
    "\n",
    "\n",
    "for col in list_of_nominative:\n",
    "    get_boxplot(col)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we can see a lot of parameters have an influence on tha main parametr - score.  So we need to make statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>famsize</th>\n",
       "      <th>parents_status</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>mother_job</th>\n",
       "      <th>father_job</th>\n",
       "      <th>reason</th>\n",
       "      <th>guardian</th>\n",
       "      <th>traveltime</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>school_suppport</th>\n",
       "      <th>family_support</th>\n",
       "      <th>paid_additional_classes</th>\n",
       "      <th>additional_activities</th>\n",
       "      <th>nursery</th>\n",
       "      <th>higher_education</th>\n",
       "      <th>internet</th>\n",
       "      <th>romantic</th>\n",
       "      <th>family_relationship</th>\n",
       "      <th>freetime</th>\n",
       "      <th>goout</th>\n",
       "      <th>health</th>\n",
       "      <th>absences</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>A</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>teacher</td>\n",
       "      <td>course</td>\n",
       "      <td>mother</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>course</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>LE3</td>\n",
       "      <td>T</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>10.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>health</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>mother</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>GT3</td>\n",
       "      <td>T</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>other</td>\n",
       "      <td>other</td>\n",
       "      <td>home</td>\n",
       "      <td>father</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  sex  age address famsize parents_status  mother_education  father_education  \\\n",
       "0   F   18       U     GT3              A               4.0               4.0   \n",
       "1   F   17       U     GT3              T               1.0               1.0   \n",
       "2   F   15       U     LE3              T               1.0               1.0   \n",
       "3   F   15       U     GT3              T               4.0               2.0   \n",
       "4   F   16       U     GT3              T               3.0               3.0   \n",
       "\n",
       "  mother_job father_job  reason guardian  traveltime  studytime  failures  \\\n",
       "0    at_home    teacher  course   mother         2.0        2.0       0.0   \n",
       "1    at_home      other  course   father         1.0        2.0       0.0   \n",
       "2    at_home      other   other   mother         1.0        2.0       3.0   \n",
       "3     health      other    home   mother         1.0        3.0       0.0   \n",
       "4      other      other    home   father         1.0        2.0       0.0   \n",
       "\n",
       "  school_suppport family_support paid_additional_classes  \\\n",
       "0             yes             no                      no   \n",
       "1              no            yes                      no   \n",
       "2             yes             no                      no   \n",
       "3              no            yes                     yes   \n",
       "4              no            yes                     yes   \n",
       "\n",
       "  additional_activities nursery higher_education internet romantic  \\\n",
       "0                    no     yes              yes      yes       no   \n",
       "1                    no      no              yes      yes       no   \n",
       "2                    no     yes              yes      yes       no   \n",
       "3                   yes     yes              yes      yes      yes   \n",
       "4                    no     yes              yes       no       no   \n",
       "\n",
       "   family_relationship  freetime  goout  health  absences  score  \n",
       "0                  4.0       3.0    4.0     3.0       6.0   30.0  \n",
       "1                  5.0       3.0    3.0     3.0       4.0   30.0  \n",
       "2                  4.0       3.0    2.0     3.0      10.0   50.0  \n",
       "3                  3.0       2.0    2.0     5.0       2.0   75.0  \n",
       "4                  4.0       3.0    2.0     5.0       4.0   50.0  "
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's update the lists of nominative and numeric columns for further analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['sex', 'age', 'address', 'famsize', 'parents_status',\n",
       "       'mother_education', 'father_education', 'mother_job', 'father_job',\n",
       "       'reason', 'guardian', 'traveltime', 'studytime', 'failures',\n",
       "       'school_suppport', 'family_support', 'paid_additional_classes',\n",
       "       'additional_activities', 'nursery', 'higher_education', 'internet',\n",
       "       'romantic', 'family_relationship', 'freetime', 'goout', 'health',\n",
       "       'absences', 'score'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "list_of_numeric = ['age', 'traveltime', 'studytime', 'failures',\n",
    "                   'freetime', 'goout', 'absences', 'score']\n",
    "\n",
    "list_of_nominative = ['sex', 'address', 'famsize', 'parents_status',\n",
    "                      'mother_education', 'father_education', 'mother_job', 'father_job',\n",
    "                      'reason', 'guardian', 'school_suppport', 'family_support', 'paid_additional_classes',\n",
    "                      'additional_activities', 'nursery', 'higher_education', 'internet',\n",
    "                      'romantic', 'family_relationship', 'health']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Statistically significant differences were found for the column: sex\n",
      "Statistically significant differences were found for the column: address\n",
      "Statistically significant differences were found for the column: mother_education\n",
      "Statistically significant differences were found for the column: father_education\n",
      "Statistically significant differences were found for the column: mother_job\n",
      "Statistically significant differences were found for the column: paid_additional_classes\n",
      "Statistically significant differences were found for the column: higher_education\n",
      "Statistically significant differences were found for the column: romantic\n"
     ]
    }
   ],
   "source": [
    "def get_stat_dif(column):  # Function to count statistics\n",
    "    cols = students.loc[:, column].value_counts().index[:]\n",
    "    combinations_all = list(combinations(cols, 2))\n",
    "    for comb in combinations_all:\n",
    "        if ttest_ind(students.loc[students.loc[:, column] == comb[0], 'score'],\n",
    "                     students.loc[students.loc[:, column] == comb[1], 'score']).pvalue \\\n",
    "                <= 0.05/len(combinations_all):  # The bonferroni correction\n",
    "            print('Statistically significant differences were found for the column:', column)\n",
    "            break\n",
    "\n",
    "\n",
    "for col in list_of_nominative:\n",
    "    get_stat_dif(col)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Statistically significant differences were found for the column: address\n",
      "Statistically significant differences were found for the column: mother_education\n",
      "Statistically significant differences were found for the column: father_education\n",
      "Statistically significant differences were found for the column: higher_education\n",
      "Statistically significant differences were found for the column: romantic\n"
     ]
    }
   ],
   "source": [
    "def get_stat_dif(column):\n",
    "    cols = students.loc[:, column].value_counts().index[:]\n",
    "    combinations_all = list(combinations(cols, 2))\n",
    "    for comb in combinations_all:\n",
    "        if ttest_ind(students.loc[students.loc[:, column] == comb[0], 'score'],\n",
    "                     students.loc[students.loc[:, column] == comb[1], 'score']).pvalue \\\n",
    "                <= 0.04/len(combinations_all):  # The bonferroni correction\n",
    "            print('Statistically significant differences were found for the column:', column)\n",
    "            break\n",
    "\n",
    "\n",
    "for col in list_of_nominative:\n",
    "    get_stat_dif(col)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1e5ce2cf548>"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAfEAAAFcCAYAAADYsIdNAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjMsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+AADFEAAAgAElEQVR4nOzdd3wUZf7A8c+zu+m9kAQSOqEmkNB7s4ARBQT07myIiL2e56mnInjCeWI/T3+ABRUbKAECByqIFOlSEwgJIYEQSCC9J7v7/P6YJckmS0myIQl53q/XvsjMPDPznYdn9pnnmWd2hJQSRVEURVGaH11jB6AoiqIoSt2oSlxRFEVRmilViSuKoihKM6UqcUVRFEVpplQlriiKoijNlKrEFUVRFKWZUpW4oiiKotSTEOJTIUSGEOLwRZYLIcT7QohEIcRBIURfe+xXVeKKoiiKUn+fA+MvsfwmINTymQV8ZI+dqkpcURRFUepJSrkZyLpEkonAF1KzA/AWQrSu735VJa4oiqIoDS8YOFVlOtUyr14M9d3AtWKNQ7dm9fuz2RuPNnYItZKW0ayyF4ChPYobO4Ra25Po2tgh1EpIYPMrF0Eeza9cLIkuaewQam3Ri36iIbZb1+/6CcZjD6J1g1+wUEq5sBabsHU89T4BVCWuKIqitBjCoW7XBrJcLgRqU2lXlwq0rTIdAqTVY3uA6k5XFEVRWhCdQdTpYwergHsso9QHA7lSyjP13ahqiSuKoigthnBomLarEOIbYDTgL4RIBWYDDgBSyo+BtUAUkAgUAffZY7+qElcURVFaDDu1qmuQUv75Mssl8Ki996sqcUVRFKXFqOs98aZKVeKKoihKi9FQLfHGoipxRVEUpcVQLXFFURRFaaautZa4esRMURRFUZop1RJXFEVRWgyhv7Za4qoSVxRFUVoMnarElSvRe9E8AqJGU5aRyebIWxotjsTDW1j/zetIs5nIEVMZFjXLarmxvIyVn/ydMymxuLh7M+XBt/H2D8FkLCdmyUucORmH2WSi99CJDI96EGN5KUveuAujsQyz2USPfjcyeuITdo1ZSsmOmHmcit+MwdGZkVPm4R/cq0a686dj2bz8BYzlpbTtNpLBE15ECMGJQ+v4Y8N/yDmXxK0Pf0+rkLCKdbLOxLM1ejblpQUIoePWR5ZhcHCyW+yH/tjGN58sQJpNjLh+MlFTrH/PYf3Kr9jyywr0ej3unj7c99hs/APaAPDO3Ec5Hn+I0B4RPPnS+3aL6YKTR7ewdZVWFnoMnErfsdZlwWQsY8O3f+dcaizOrt7ccNfbePqGAPDHxv/jyK4fEDodwyf+g3bdRpCdkcTPXz1TsX5e1ikGjHuCPiPu5fzpI/z246uYykvR6fWMmDybwHa97XYsxw5uYc1X8zCbzfQfNZVRtzxgtfzE0d2sWTqf9FPHuOORtwgbOK5i2edvPsCp4wdoH9qXe/76sd1iupSmXC4u5U83uBLe2ZEyo+Sz1QWcTDfVSDNplAtDwp1wddbx+ILKl3gNDXdi6nWu5OSbAdi4p4StB0qvWuwXI3TXViWu7ok3kNQlP7JrwsxGjcFsNrFu6Vz+8tQiHn4thsO71nAuLdEqzf6ty3F28+Sx+T8x6IZ72bD8LQDi9q7DaCznoTmreeDlH/jjt+/IOZ+K3uDI3c9+zoOvrmTWKys4fngrqcf32zXu1GObyctMYdpf1zF80hx+XznXZrptK+cwbPIcpv11HXmZKaQe2wKAT2Ao1935AUEd+lvnh8nIpmXPMWzSq0x5KoaoB5ag09vvOtZsMrF04Rs8/fIHvPb+D+zcuo60U0lWadp36sbLC75izrvf03/o9Sz/4r2KZeMm3cPMp16zWzxWsZlNbFkxlwn3L+JPz8aQuH8NWenWZeHIruU4uXhy5/M/0XvkvexYq5WFrPREEvev5U/PxjBh5mK2/DgXs9mET0Anbn8mmtufiWbqUz9gcHChU9j1AGxf8yb9b3iU25+JZsCNT7BjzZt2PZbVX7zGvc8u5Ml/rebgjjVknLY+Fm+/Nkx9YD69h9xcY/0RUTOY+uAbdovncppyubiUsM4OBPjq+cfHOXy5tpA7x7vZTHcwoZx5n+XaXLY7roy5n+Qy95PcJlGBAwi9rk6fpqrpRtbMZW3dQ3mW7YJ9taSdOIhPQDt8WrVFb3Ck18Ao4vdvsEoTv38DfYZOAqBnv3GcOLodKSUCQXlpEWaTkfLyEvQGB5yc3RFC4OisncxmkxGzyYgQ9r2yTYnbSJfIiQghCGgXQVlJHkV5GVZpivIyKC8pILBdJEIIukROJCVOOzbvgM54t+pYY7unE7fhG9QNv9bdAXB29UGn09st7qSEwwS0DqFVUAgGBwcGDh/Hvl2brNJ0Dx+Ak5MLAJ26hpOdWXlcPXsPwtnF9hdlfWWcPIiXfzs8/bSy0CUiiuRY67KQHLuBbv20stA5fBynE7SykBy7gS4RUegNjnj6huDl346Mkwet1j2dsB0vv7Z4+GhvVhRCUF5SAEBZST6ungF2O5bU4wfxDWiHb0BbDAZHeg+O4sgfG63S+LQKJqhdN4So+RXXudcQnJwbJp9tacrl4lIiujqy45BW8SalGXF11uHlVvNcT0ozklvYfN5Gp9OLOn2aqmbTnS6EiEZ7A4wz8J6UcqEQ4n7g72hvgkkASqWUjwkhWgEfA+0sqz8lpdzWGHE3przsdDx9Kt857+kTxOmkA1Zp8rMzKtLo9AacXTwoLsihR79xxO/fyDt/HUF5WQk33vE8Lu7egNYSWvzaFLIyTtJ/zF8I7tTHrnEX5aXj5hVUMe3qGURhXoZVRVCYl4GbV2DFtJtnIEV56Zfcbu75ZADWfTaTksIsOvWOovdI+/WW5GSdw9e/Mm4fvwBOHDt80fRbf4kmrO8wu+3/Ugrz0nHzriwLbl5BZJy0LgsFuRm4e1eWBUdnD0qKcijMTSewXYTVuoXV8jrxwFq6RFa2eofd+iIxi2fye8y/QZqZ/Ng3djuWvOwMvPwq89nTN5BTxw9eYo3G1ZTLxaX4uOvIyjNXTGfnm/H20JFbWLNL/WL6dnekazsD6Vkmvvu5iOx88+VXamCqO73xzJBS9gP6A08IIYKBl4HBwA1A9ypp3wPekVIOAKYAi21tUAgxSwixRwixZ505p2GjbyKqt5qlrdfZCkg7cQidTsdTCzbz+L9+YftPn5F9TnufvU6nZ9bsaJ56cxNpJw6ScfqYXWO0FVPN1r6tuC99ckqzifSUPxh9+5tMmLWU5NhfSEvcXo9Iq21fXnlM2zetIfl4HOMn3WO3/V+SrYbSFeSpAGwdVtVXI5uMZSTHbqRz7/EV82K3f8PQW57nnpc2MfTWF/j1+5fqErVNNsuHzVc1Nw1Nulxcio0Qa9PePpBYxgsfZjNncS5HTpQz4xZ3u4VWH6ol3nieEEJMtvzdFrgb+E1KmQUghFgGdLUsvx7oWeWL31MI4SGlzK+6QcsL3RdC3V8U35R5+gSSl135pru87LO4ewfYTOPpG4TZZKSkOB8XN28O74qhc9gI9AYH3Dz9aNulL2nJh/FpVfk6XGdXT9p3G8jxw1sICO5KfcRtX0r8nuUA+AeHUZh7tmJZUd5ZXD1aWaV38wykMLeyNViYl46rx6W7bF09A2ndcQDObj4AtO02kvNpcbTpMqResV/g4xdA1vnKuLMzM/D2bVUjXdyBnaxZ/gnP/XMxDg6Odtn35bh5BVKYU1kWCnPP4lati9vdK5CCnDO4e2tloawkHydXb9y9AynIvfi6J49uwT+4J64e/hXz4vdGM2ziPwDo3Hs8m5bZrxL38gkkN7Myn/Oy0vH0sV93vb015XJR3eh+ToyMcAbgRJoRX8/Kdp6Ph47cWrSkC4srv1I37y/ltjGu9gu0Hq61R8yaRUtcCDEarWIeIqXsA+wD4i+xis6SNsLyCa5egbcEbTqEk5WeQva5VEzGMmJ3raVrn7FWabr2GcuB36MBiNu7ng7dByOEwNO3NclHdiClpKy0iNNJB/AP6kRhfhYlRXkAlJeVcOLIdvyCOtU71p5D7mTy4yuY/PgK2ve8jsR9K5FSknFyPw7OHjXuqbp6BuDg5EbGyf1IKUnct5L2PcdeZOuakK7DyTobj7GsGLPJyNkTu/EO6Fzv2C/oGNqL9DOnOJd+GmN5Obu2ridiwCirNClJR/nio9d5/MV38fT2tdu+LyegbTg551PIy9LKQuL+tXSoll8deo4lfq9WFo4fWk9wF60sdOg5lsT9azEZy8jLSiXnfAoBVUaaJ+5fQ2ik9QAyV88A0pJ2AXA6cQde/u3tdizBncLJTE8h61wqRmMZB3espXvkGLtt396acrmobtPe0oqBaPuPlTE4XHtyo1MbA8Wlslb3vqveP48IdeRs5pV3wzckodPV6dNUCZtdPU2MEGIiMFNKeYsQojuwH7gfeB2IBPKBDcAhyz3xr4F9Uso3LetHSCkvOYTa3i3xiC/fwm/UQBz9fShNzyRh7gec+my53bafvfHoFaVLOPgbP303D2k202fYFEZMeIhN0e/TukMY3SLGYiwvJXrxc5w9eQQXNy9ue/BtfFq1paykkFWfvci5M8dBSvoMu42h4+8n/VQ8Kz99Hmk2IaWk54DxjLzl8m/XS8u48uyVUrJ91WukJmzF4ODMiCnzKh4TW/HBZCY/vgKAc6mH2bz8BUzGUkK6jmDILS8hhCA59me2r36dksIsHJ098WvTnfH3aXdUEvet4sBvCwFB224jGXjT3y4ax9AexVcc8wUH927l208WYDabGX7drUyYNpPorz+iQ5eeRAwcxYLZD3E6JREvH63V6tsqiCdefBeAf704gzOnkyktKcbdw4vpj75CWOTQWu1/T+LFWzspR35j2yqtLHQfOIV+1z3ErvXv0yokjI69tLKw4dvnOH/6CM6uXtxw59t4+mk9L3s3fMzRXT8g9HqG3foi7buPBKC8rJgvXx/Nnc//gpOLR8W+zpzYy9aVryPNJvQGJ0be9orVo34XhATW7bSLP/Aba76aj5Rm+o68jTG3PsQvP7xPcMcwevQdS2rSIZa+9zjFhXkYHBzx8PbnyfkxACz8512cO5NEWUkRru7e3Hb/PwntPfyK9x3k0fzKxZLoklrHDPCXcW706uRAWbnk85gCUs5qFfEr93sx9xNt4O6UMa4M6uWIl6WlvuVAKau3FDN5tCsRoQ6YzFBYIlm6roCzmVfekl/0ol+DNJn/uG54nQpd3w1bm2QTvrlU4k5ANBCM1gJvBbyK1n3+LNrAtiNAlpTyH0IIf+BDoAfaLYPNUsqHLrWP5tadfqWVeFNRm0q8qahLJd7YLlWJN0V1rcQbU10q8cZW10q8MTVUJb7/xhF1KnQRP21pkpV4s7gnLqUsBW6qPl8IsccySt0ArAB+sqQ/D9xxdaNUFEVRmrprbXR6s6jEL+FVIcT1aI+d/YTWWlcURVEUm5ry/e26aNaVuJTy2caOQVEURWk+VEtcURRFUZqppvzMd12oSlxRFEVpMa61lvi1dXNAURRFUVoQ1RJXFEVRWgw1sE1RFEVRmqlrrTtdVeKKoihKi6EqcUVRFEVpplQlriiKoijNlLonriiKoijNlHpO/BrV3F4o4jO2e2OHUCt739nb2CHUWqyHe2OHUGtG45W/JaopyM5vfq2i46dcGjuEWmsT0jjvJ2+KVHe6oiiKojRTqjtdURRFUZop1RJXFEVRlGbqWqvEr61+BUVRFEW5BKHT1elz2e0KMV4IES+ESBRCPG9jeTshxK9CiH1CiINCiCh7HI9qiSuKoigtRkO0xIUQeuBD4AYgFdgthFglpYyrkuwl4Hsp5UdCiJ7AWqBDffetKnFFURSlxWiggW0DgUQpZRKAEOJbYCJQtRKXgKflby8gzR47VpW4oiiK0nKIurXEhRCzgFlVZi2UUi60/B0MnKqyLBUYVG0TrwI/CSEeB9yA6+sUSDWqElcURVFajLp2p1sq7IUXWWxro7La9J+Bz6WUbwkhhgBfCiHCpJT1+nEHVYkriqIoLUYDdaenAm2rTIdQs7v8fmA8gJRyuxDCGfAHMuqzYzU6XVEURVHqZzcQKoToKIRwBP4ErKqW5iRwHYAQogfgDJyr745VS1xRFEVpMRpidLqU0iiEeAxYD+iBT6WUsUKIucAeKeUq4K/AIiHE02hd7dOllNW73GtNVeKKoihKi9FQP7sqpVyL9thY1XmvVPk7Dhhm7/2qSryWEg9vYf03ryPNZiJHTGVY1Cyr5cbyMlZ+8nfOpMTi4u7NlAffxts/BJOxnJglL3HmZBxmk4neQycyPOpBjOWlLHnjLozGMsxmEz363cjoiU80yrH1XjSPgKjRlGVksjnylkaJwZbJIxzp0d5AuVHyzYZSUs/VHAcSNdiR/t0MuDoJnl9YWDG/Uxsdk4c70dpfx5frSzhw3GT3+E7EbWbTD69jNpsJHzKNgTfWLBPrvnyO9FOxuLh5c/N97+DlF1KxPC8rjSWv38yQqMfof939AKxf+gJJhzfh6uHHvS/G2D1mKSXbV8/jVPxmDI7OjJo6D//gXjXSnTsdy2/LXsBUXkrbbiMZcsuLCCFIOrSOvb/8h5xzSUx65HtahYQBkJqwjd3r3sZkKkevd2Bg1N8I7jzYLjGfiN3MxuXauRc+bBqDbOTz/754jvSTsTi7eXPL/TXz+bPXbmbozY8x4Hotn/f+uoSD25aBlPQeNo1+Y6fbJVbQ8njnGkseOzgzYortPD5/OpYtP7yA0ZLHg27W8njX/97k1NFf0ekd8PBty4gp83By8eR04jb2rH8bs6kcnd6BAeP/Rhs75THATQN0hAbrKDdB9DYjZ7JqpmntC5OHGTDoIeG0mf/t1s7J0X109AvVUViipduwz0TCaYlOwMShelr7CnQCDiSZ2XK4cV7W06J+sU0I4S2EeKShgxBCJAsh/KvvTwjRRgixvKH3f6XMZhPrls7lL08t4uHXYji8aw3n0hKt0uzfuhxnN08em/8Tg264lw3L3wIgbu86jMZyHpqzmgde/oE/fvuOnPOp6A2O3P3s5zz46kpmvbKC44e3knp8f2McHqlLfmTXhJmNsu+L6dFeTytvHfO+KuL7X0uZOsrJZrrYE0beXVZcY352vuTrDaX8cczYIPGZzSY2LpvL5IcXM/0fazi6N4bMM9Zl4vD2ZTi7enL/7J/pO2Y6W1YusFq+6cf5dOg5wmper0G3cdsjixskZoBT8ZvJzUzh9mfXMXzyHLZGz7WZblv0HEZMnsPtz64jNzOF1GNbAPAJDOWGuz6gdYf+Vumd3Xy48d6PmPrUKkZNm8+m7/9ul3jNZhO/fD+XKY8u5r6X13B0Twznq+XzIUs+z5zzM/3HTmdztHU+//rDfDr2qsznc2nHOLhtGXc9t4x7X1zJ8cObyM5Itku8AKnHNpN7PoWpz6xj2KQ5/L7Kdh7/vnIOwybNYeoz68g9X5nHwV2GMvmJVUx+YiVe/h04+Js2MNrZ1Ycb7v6IyU+sYuTU+WxeZp88BggNFvh5Ct6PNrJ6u4kJg/Q2000YrGfVdhPvRxvx8xR0aVNZMW6PM/NxjJGPY4wknNZ6i3t1EOh18N/VRv5vjZF+XXV4u9kt7FoROlGnT1N1uX4Fb6BGJW75dZqGYLU/KWWalHJqA+2r1tJOHMQnoB0+rdqiNzjSa2AU8fs3WKWJ37+BPkMnAdCz3zhOHN2OlBKBoLy0CLPJSHl5CXqDA07O7gghcHTWSrPZZMRsMiLq+BxjfWVt3UN5Vm6j7Ptiwjoa2H1Uq4BT0s24OAk8XWvmT0q6mbyimreXsvMlZzLN1P/Ok21nUw7i7d8eb3+tTHTvdzPHD1mXieOHNtJz0GQAukaM4+QxrUwAJB74BS//EPxah1qtE9JlAM6uXg0TNJByZCOhkRMRQhDYLoKykjyK8qwHyRblZVBWWkBg+0iEEIRGTiQ5Tjs2n4DOeLfqWGO7/m164uYZoKUJDMVUXorJWFbveM8mH8SnVbV8Plgtnw9upNeFfI4cx8n4ynxOOPALXn7W+Zx19jhtOvbBwdEFnd5A29ABJBz4ud6xXnDyyEa6WPI44BJ5XF5aQEA7LY+7RE7k5BHtuIJDh6HTa52lrdr2oTAvHQC/Nj1xteSxd0AoJqN98hige1vB/uNaCzn1vMTZUeBe7c2r7i7g5CBIPa/l7f7jZnq0u/R3lpTgaACdAIMBTGYoLbdLyLWn09Xt00RdLrJ/AZ2FEPuFELstv/v6NXAIQAgRLYTYK4SItTwIjxDiYSHEvy9sQAgxXQjxgeXvu4QQuyzb+z8bFwNV9/emEKKDEOJwle1ECyFWCyFOCCEeE0I8Y/kd2h1CCF9Lus5CiHWWuLYIIez24u287HQ8fVpXTHv6BJGfnW6VJj87oyKNTm/A2cWD4oIcevQbh4OTK+/8dQTvPzeWITfOwMXdG9BaGQvnTOKtZ4bRsedQgjv1sVfIzZ6XuyCnoLLbLafAjJd707kqLshJx8MnqGLa3TuQ/BzrMlGQm46Hd2WZcHLxoKQwm/LSInb/soghNz12VWMGKMxNx927Mm43ryAKq1UwhXkZuHkGVkkTSGGu9bFdyonDP+HXpgd6Q/3fZZ1/BfmspanMZ0cXD4oLsykrLWLXz4sYGmWdz/5tupKauIfigmzKy4pJit1MfvbZesd6QVFeOm5eVfLYM8hmJe7qZZ3HRXk18zhh74+EdB1RY35y7E/42imPATxcBXlFldN5RbLGRbOnq7C6YM4r0ta7YGB3HQ/fYmDiUD3OlrDiUiRlRnh2moFnbjPwe6yJYvtcd9SaEKJOn6bqcvfEnwfCpJQRQojRwBrL9AnL8hlSyiwhhAvab8X+ACwHtgPPWdLcAbxuGVJ/BzBMSlkuhPgvcCfwha39AQghOlSLJwyIRBuanwj8XUoZKYR4B7gHeBftYfyHpJQJQohBwH+BsbYOruov8Nz37MeMvXWWrWSXVP0/V9Z4vh8QkHbiEDqdjqcWbKakKI/P37iTjj2H4tOqLTqdnlmzoykpyuP7Dx8j4/QxAoK71jqWa5HNX1BooFZ13dQMpsYJbytgIfh97Qf0HXMvjk6N0a9oOybrJFdwbBeRlZ7ArnVvETXDXrcE6pbPAsHvaz6g35h7K3q8LvAL6szAG2ay7D8zcHR0JSC4Gzqd/ToZbQ48vpLvi2qlfv+vHyN0ejr3sR6nkp2ewJ71bzFuuv1uu9g+367ghLMk2R1v5reDZpAwNkLHuP56Vv5uIthfICUsWGbExQlmjDOQdMZIdoHdQr9iLf194ruqVOAATwghJlv+bguESil3CCGShBCDgQSgG7ANeBToh1bZA7hQ+4fcf5VS5gP5QohcYLVl/iGgtxDCHRgKLKtygtu+iYr1L/B8teXyJdXTJ5C87DMV03nZZ3H3DrCZxtM3CLPJSElxPi5u3hzeFUPnsBHoDQ64efrRtktf0pIP49Oq8vcBnF09ad9tIMcPb2nRlfiwcAeG9NSK5skMM97uOkBrjXu768grbDq1uLt3kFXrrSAnHXevgJppcs7g4aOVidLifJxdvTmbfICE/evZsnIBpcV5IHToDU5EjrqrQWKN3b6Uo7u1ISatQsIoyKmMuzD3LG4erazSu3kFVnThamnSK7pxL6Ug9yw/f/k4o6f9C0+/dnaJ3eMK8tnDJ4j87Mp8LivOx9nNmzPJBzi2bz2bo7V8FpZ87jv6LsKHTiN86DQAtqx8G3efQOojbsdSjlny2D8kjMLcKnmcdxbX6nnsGUhR7sXzOOGPaE7Fb+KmGZ9ZXbQU5p5lw9LHGTm1/nk8sJuOvqFaxZaWKfF0rVzm6SrIrzbUpHrr3NMV8ou1c/LCgDaAvQlm/jJWO497dxQkpJkxSy3NyXOSNn6C7IKrfy435fvbdVHbSrxi2K+lZX49MERKWSSE2ITWQgb4DrgdOAqskFJKoZXAJVLKF+oRb2mVv81Vps1ox6IDci605O2tTYdwstJTyD6XiqdPALG71jL5AevBM137jOXA79GEdI4kbu96OnQfjBACT9/WJB/ZQfjgWykvK+Z00gEGXX8vhflZ6PUGnF09KS8r4cSR7Qwd37QGl11t2w6Vs+2QdsOsZ3s9w3s7sC/BSPtAHcVl0ua978YS1C6cnHPJ5J4/hbt3IEf3riFq+ltWaTqHjyVu5wradIzk2P71tOuqlYk7nv66Is3vaz/A0cm1wSpwgF5D7qTXkDsBOHl0E7Hbv6ZznygyTh3A0dmjRgXt6hmAg6Mb6Sf3E9C2Dwn7VlasfzGlxXms//whBo5/hqAOfe0We1D7cLIzksk5fwoPSz7fbCOfY3euoE2nSI7tW09bSz7/+ZnKfN62RsvnvqO1fC7Mz8TNw4+8rDQSDvzEX579rl5x9hx8Jz0Ha3l06ugm4nZ8TafeUZw7dQBHp4vksZMbGSf306ptHxL3raSnJY9Tj23h0ObF3PTAFxgcK29Mlxbn8dMXD9H/xmcIbF//PN4Vb2ZXvHaRHBosGNRdx+FkEyH+gpJySUG1SrygGMrKJSH+2n3xiM46dh7V1nd3oSJ9j3Y6MnK0czW3EDoF6TiYZMLBACH+gh1xjXQet7CWeD7gcZFlXkC2pQLvDlR9xuFH4B9ACnBh6OQGYKUQ4h0pZYblHraHlDLlCvd3WVLKPMv98mlSymWWC4feUsoDdd1mVTq9gfF/eZmv370faTbTZ9gUAoJD2RT9Pq07hNEtYiyRI6YSvfg5/vPCjbi4eXHbg28DMGDMX1j12Yt8PPsWkJI+w24jsG030k/Fs/LT55FmE1JKeg4YT9c+Y+wRbq1FfPkWfqMG4ujvw9gTv5Ew9wNOfda4DwfEpZjo0V7PP+52pcwo+XZD5XXcs3e4sOA77RvjlqGO9O1qwMEBZk93ZUeckfW7ymgboGNGlDMuToJeHQ2MH2jmjW9qjmKvK53ewJhpr/DDf2cipYmwwVPwbx3KtjXvEdQujM7h1xE2ZCr/++JvfDLnBpxdvbj5vncuu901nz1DauIuiguyWfjySIZEPU74kGl2i7ttt1Gcit/MdwvGYXDQHjG74If3JzPliRUADJ80m8yf9msAACAASURBVN+WWx5/6jqCtt1GAnAi9me2r3qd4sIs1i95CN/W3YmasZjY7UvJyzzJHxs/4o+NHwEQNWMxLu5+9YpXpzdw3e2v8MOHMzGbTYQPmYJ/m1C2xmj53KX3dYQPncraJX9j8ewbcHbzYsKMy+fzqkWPU1yYg15v4LrbZ9t1MGFIt1GcOraZ5W9reTzitso8jv5gMpMe1/J46K2z2fzDC5iMpYSEjiCkq5bH21f/E7OpjPWfao/DtWrbh2GTXuXIjqXkZ55k/68fsf9XLY/H3Vf/PAZIOC3pGix5crKBciNE/175SOZDEwx8HKMNMo3ZaWbSUD0OBu0Rswuj0G/sqyfIVyCBnALJ6h3a+rvitfSP3qpVOfuPm0nPqXe4dXKttcTF5e53WAay9QaKgXQp5QTLfCcgGu3tLfFAK+BVKeUmy/IYoKeUslOVbd0BvIDWYi4HHrV0vycD/aWU56vs739o72eNkVKGCSGmW9I8ZtlW1XUqlgkhOgIfAa0BB+BbKaXtZzuquJLu9KbEZ6zdxutdFb+8s7exQ6i17l3dGzuEWssvaJxnb+vKy7P5tYqycppXHgMUFdn/9xEa2px7HBqkts1+/eE6fdf7/OOjJln7X7Y7XUr5l4vMLwVuusR6E2zM+w6tq736/A6X2F+YZf7nwOcXWadimeWe/fiLxaUoiqK0YNdYS1z9YpuiKIrSYrT00emKoiiK0mxda/fEVSWuKIqitBxCtcQVRVEUpVm61lri19YliaIoiqK0IKolriiKorQcamCboiiKojRPTfllJnWhKnFFURSl5VAtcUVRFEVpnq61gW2qElcURVFaDvWImaIoiqI0U6olfm1Ky2hW7z9hbzN7ocj1T/dr7BBqbcWr2xo7hFpzcXNs7BBqxdfX5fKJmhhDw7yXo0GFddU3dghNhlAtcUVRFEVpplRLXFEURVGaJ/UCFEVRFEVprtRz4oqiKIrSTKmWuKIoiqI0U6olriiKoijNk7onriiKoijNlXrETFEURVGaKfWImaIoiqI0T9faj71cW0ejKIqiKC2IqsQVRVGUlkMn6va5DCHEeCFEvBAiUQjx/EXS3C6EiBNCxAohvrbH4ajudEVRFKXlaIDudCGEHvgQuAFIBXYLIVZJKeOqpAkFXgCGSSmzhRAB9ti3qsRrQUrJjph5nIrfjMHRmZFT5uEf3KtGuvOnY9m8/AWM5aW07TaSwRNeRAjBiUPr+GPDf8g5l8StD39Pq5CwinWyzsSzNXo25aUFCKHj1keWYXBwsvsxTB7hSI/2BsqNkm82lJJ6zlwjTdRgR/p3M+DqJHh+YWHF/E5tdEwe7kRrfx1fri/hwHGT3eOrjd6L5hEQNZqyjEw2R97SqLFU9ecb3Qjv7EhZueTTmHxOnq2ZT5NHuzIk3AlXZx2PvZlptax/D0duHeGKBFLTjSxaWdDgMU8Z5USvjg6UlUu++qnYZrmYMNSJgT0ccHUSPPvf/Ir5YyIdGRLmgNkMBcWSpT8Xk53fMC8UummAjtBgHeUmiN5m5ExWzTStfWHyMAMGPSScNvO/3dqxjO6jo1+ojsISLd2GfSYSTku83eCxiQbO52nzU8+ZidlZ8/jrYlxfHV3aCMpNsGqHibPZNdME+cDEwXoMekhMk6z/wxJvuI6uIQIpobBEsmqnmYJicHKASUN0eLkKdDrYfsTMgRP2z+9jB7ewduk8zGYz/UZNZdSEB6yWnzi6m7Vfzyf91DFuf+QtwgaMq1i2ZMEDnDp+gPahfbn7mY/tHlu9NMxz4gOBRCllkrYL8S0wEYirkuYB4EMpZTaAlDLDHjuu8yWJEOIpIYRrHda75DeSECJCCBFVZfrWi3VNXG2pxzaTl5nCtL+uY/ikOfy+cq7NdNtWzmHY5DlM++s68jJTSD22BQCfwFCuu/MDgjr0t0pvNhnZtOw5hk16lSlPxRD1wBJ0evtfX/Vor6eVt455XxXx/a+lTB1l+yIh9oSRd5cV15ifnS/5ekMpfxwz2j22ukhd8iO7Jsxs7DCshHd2IMBXz4sfZfPF2gLuGu9uM92BY2W8/llOjfkBPjqihrryry9ymb0wh29/LrSxtn317GAgwEfP3M8L+HZDCXdcZ/vNYoeTjCz4pmY8qedMvPlNIf9aWsj+xHImjXBukDhDgwV+noL3o42s3m5iwiDbb+aaMFjPqu0m3o824ucp6NKm8kt7e5yZj2OMfBxjJOF0ZcWXlU/FfHtV4F1aC3w94MMYE2t2mYjqbzveqAF6YnaZ+DDGhK8HdG6txfv7ETML/2di0ToTCWmSkb20r+v+oYLzubBwnYkvNpi4IVJn9x8hM5tNrP7iNe7560KemL+aQzvWkHE60SqNt18bpsycT+/BN9dYf/hNM5g66w37BmUvOl2dPkKIWUKIPVU+s6psNRg4VWU61TKvqq5AVyHENiHEDiHEeLscTj3WfQqodSV+BSKAikpcSrlKSvmvBthPraXEbaRL5ESEEAS0i6CsJI+iPOuLqaK8DMpLCghsF4kQgi6RE0mJ2wCAd0BnvFt1rLHd04nb8A3qhl/r7gA4u/qg09n/1YFhHQ3sPqpVwCnpZlycBJ6uNa9KU9LN5BXVvLLPzpecyTQjm8hbW7O27qE8K7exw7AS0dWR7Qe1pl5SmhFXZ4GXe808TkozkltQMyNHRjrz695iikq0Zfk2/h/sLbyzgV1HygBIPmvCxRGb5SL5rMlmuUhINVFuua5LPmPC28bx2kP3toL9x7UKNvW8xNlR4F7tesPdBZwcBKnntTj3HzfTo13jPFLUNURwMFmL43QmODuCe7XrG3dnrWV92tIZczBZ0i1Ei7esyrWyowGq5ryjQ+X84jIw2+e6o0Jq0kH8AtvhG9AWg8GR8EFRHPljo1Uan1bBBLXrZvPHUzr3GoKjs5t9g7IXoavTR0q5UErZv8pnYdWt2thT9ZPFAIQCo4E/A4uFEN71PZwrau4JIdyA74EQQA8sA9oAvwohzkspxwghCqSU7pb0U4EJUsrpQoiOwNeWfa2rss0vgeVSypWW6aXAd8BcwEUIMRyYD7gA/aWUjwkhPgeKge5Ae+A+4F5gCLBTSjndsq0bgTmAE3AcuE9KWe8+yaK8dNy8giqmXT2DKMzLwNWz8tZGYV4Gbl6BFdNunoEU5aVfcru555MBWPfZTEoKs+jUO4reI+3fwvRyF+QUVJ7tOQVmvNyFzS9mpW68PfRk5ZVWTGfnmfH20JNbcGW9F4G+2sXb8/d4IXSwanMRsUnlDRLrBd5uwqr7O6dA1rlcDOnlSFxyw/TUeLhax5RXJPF0FRQUV87zrJFGW++Cgd119OmsIy1Tsn6PiRLt2gUfd3hogoHSMsmG/WZOZtT/nPBwgbxC63g9XKGgpOoxUeOYPFwq4x3TW0d4B0FpOXy5Ubsts/uY5I6Rgqcm6XEywA+/27kGB/KyM/Dyrfyu8/QNJPX4Qbvvp1E0zHPiqUDbKtMhQJqNNDuklOXACSFEPFqlvrs+O77Slvh4IE1K2UdKGQa8awlwjJRyzGXWfQ/4SEo5ADhbZf5itEoYIYQXMBRYC7wCfCeljJBSfmdjez7AWOBpYDXwDtALCLd0xfsDLwHXSyn7AnuAZ2wFVrV7ZOfPC20lsSJrXFiBqHF/xcbJf5l7MNJsIj3lD0bf/iYTZi0lOfYX0hK3Xzae2rJ5qajqb7uy+V9di0zW6QQBvnre/CqXRSvyufdmd1ycGrYlaa9bhP27O9A2UMeGvWX22WA1trP2CvLWkmR3vJn3Vhj5eLWRgiLJOEv3dn4xvP2j1pW+bo+JqSP0ODk0VLy128avB828v8rE4RQzA0K1r+vOrQVns+HdaBML15kY30+Ho73vvtkItOZ3XTNVx5b4ZewGQoUQHYUQjsCfgFXV0kQDYwAs9VRXIKm+h3Ol//WHgAVCiDeAGCnlllr8hw4Dplj+/hJ4A0BK+ZsQ4kPLCL3bgB+klMYr2O5qKaUUQhwC0qWUhwCEELFAB7QroJ7ANsu2HAGbNaKlO2QhwL9/MNs8veK2LyV+z3IA/IPDKMytvA4pyjuLq0crq/RunoEU5la2vAvz0nH1uPQgRFfPQFp3HICzmw8AbbuN5HxaHG26DLnkeldiWLgDQ3pq/80nM8x4u+sA7crd211n1VJQ6mZMP2dGRGr9pMlpRnw9K094H0+dVe/H5WTnm0g6bcRkhvO5ZtIzTQT66kk+Y9/W7YjeDgwNdwTg5FkTPh6V5523u7DZ1X8p3drqGTfQkfeWFWG043jHgd109LVUXmmZEs8qN/A8XQX51YZuXGidV6aBfEtLvbBKC3hvgpm/jNXOC5MZii2dJ2eyICtf4ucpSMus/bnRP1QQ2blKvG4CLF37Wq+Bdfr8IqrFW/OYAA4nS/40Ssdvh6FPR8G2I1qZyi6AnEKJvyek2RjkV1eevoHkZlV+1+VlpePhbZfB1I2vAS5GLHXXY8B6tN7qT6WUsUKIucAeKeUqy7IbhRBxgAn4m5Qy8+JbvTJXVIlLKY8JIfqh3aueL4T4yVayKn9XH9lysbPhS+BOtKuWGVcSC3Chr9Jc5e8L0wa0zPlZSvnnK9zeJfUccic9h9wJwMmjmziy42s69Y7i3KkDODh7WHWlA7h6BuDg5EbGyf20atuHxH0rK9a/mJCuwzm05ROMZcXo9A6cPbGbXsPutUf4bDtUzrZDWndsz/Z6hvd2YF+CkfaBOorLpOpKt4Nf95bw616thgjv4sDY/i7siiujUxsDxaWyVhXivvgyBvVy4veDpbi7CAL99JzLsf9TAFsOlrPloFYuenUwMDLCkb3xRjoE6Skpo1blIqSVjjuuc+Gj6CKrrm172BVvZle8VmGFBgsGdddxONlEiL+gpFzWqBQLiqGsXBLir90Xj+isY+dRbX13FyrS92inIyNHi9XVSbuvLKXWre7nKeo8un5PgmRPgvb/1aWNYECoIDZFEuwHJeXWXemgTZeVQ7Cfdl+8dwfB7mPavn3dIctyE7BrsCAzT5ufWwQdA3WcOmfGzRn8PATZdn6AIbhjOJnpKWSdS8XTJ4BDO9cy7aE37buTxtJAL0CRUq5F602uOu+VKn9LtF5hmz3DdXWl98TbAFlSyq8so8unA/mAB3DekixdCNEDiAcmW5YDbEOrpL9Cq7Cr+hzYBZyVUsZa5l3Ybl3tAD4UQnSRUiZaRtCHSCmP1WObALTtNorU+M0se2scBgdnRkyZV7FsxQeTmfz4CgCGTpzN5uUvYDKWEtJ1BCFdRwKQHPsz21e/TklhFj8teQi/Nt0Zf99inFy8CBs2nZX/nQYI2nYbSbvuo+sbbg1xKSZ6tNfzj7tdKTNKvt1QeQ307B0uLPhO+4a7ZagjfbsacHCA2dNd2RFnZP2uMtoG6JgR5YyLk6BXRwPjB5p54xsbzYarJOLLt/AbNRBHfx/GnviNhLkfcOqz5Y0WD8ChxHLCOzsy7xEfysoln8VUfru+MtObuYu1EelTx7oysJcTjg7w78d92Lq/lFVbtPvfvTo5MneWN2YJyzYUUmjnirG62GQjPTsaeGW6O+VG7RGzC/5+pxtvLNVGpE8c7kS/bg44OMDc+93ZHlvO/3aUMmmEM04OMONmbZRZdp6ZhavtXy4STku6BkuenGyg3AjRv1de3Dw0wcDHMVpvRcxOM5OG6nEwaI+YXRiFfmNfPUG+Aol233/1Dm399oGCsRF6zGYwS1i9w0SxHe4IJKZJurQWPDpBj9EEq3ZWxvvAeD2L1mnTa/eYuHWQ9ojZ8TOSxDNavGMjdPh5aPHmFkrWWh6V2xJr5tZBOh68SbsdsPGA2S7xVqXXG5hw90sseXOm9ojZyNsIDAnllx/fJ7hDGD36jiU16RBfv/84xYV5HN33Kxt//IAn5scAsOj1uzh3JomykiL+/dRoJt//T0LDh9s3yLq6Vm4LWIgruackhBgHvInW2i0HHkYbTPYocMYysG0qWlf5KeAw4G5jYNsPwEsXBsBZtr0OiJZSfmyZ9kXrdnDA9sC2GCnlciFEB8vfYZb1qi4ba4nlwjNUL1m6My7qYt3pTdWZM0WNHUKtXP90v8YOodZWvLqtsUOoNRc3x8YOoVZ8fW0/ztaUGRyaXyXQvWPz+3HOaYMbZgRaydqFdfqud46a1ST/46+0O309WsVa1R7ggypplgM1mkFSyhNoFf4FFY+LWVrJocA3VdJnAQOqbeZzy7LpVdIlA2FVpqsu22hjG4qiKEpLd429T7zRjkYIcT1wFPhAStm0HvZVFEVRrk1C1O3TRDXaz65KKX8B2jXW/hVFUZQW6Bp7Fan67XRFURSl5WjCreq6UJW4oiiK0nJcY/fEVSWuKIqitBjyGmuJX1uXJIqiKIrSgqiWuKIoitJyqIFtiqIoitJMqUpcURRFUZqna+2euKrEFUVRlJZDtcQVRVEUpZlSLfFr09Aejfc2rrqI9XC/fKImpDm+TGTyq8MaO4Ray9t0tLFDqBW9rlm9dwgAR0Pzi3nB3C2NHUKtTVs9qmE2rJ4TVxRFUZTmSd0TVxRFUZTmSt0TVxRFUZTmSapKXFEURVGaKdWdriiKoijNk2qJK4qiKEpzpVriiqIoitJMqZa4oiiKojRP6hEzRVEURWmuVEtcURRFUZonybXVEr+2LkkURVEUpQVRLXFFURSlxVCPmCkVDv2xjW8+WYA0mxhx/WSiptxntXz9yq/Y8ssK9Ho97p4+3PfYbPwD2gDwztxHOR5/iNAeETz50vsNFuOJuM1s+uF1zGYz4UOmMfDGWVbLjeVlrPvyOdJPxeLi5s3N972Dl19IxfK8rDSWvH4zQ6Ieo/9192vHtfQFkg5vwtXDj3tfjGmw2C/4841uhHd2pKxc8mlMPifPmmqkmTzalSHhTrg663jszUyrZf17OHLrCFckkJpuZNHKggaP+WJ6L5pHQNRoyjIy2Rx5S6PFkXBoC+u+fh2zNNN3xFRG3FyzXKxY/HfSUmJxdfNm6sNv4+MfgtFYRsyS2aQlH0YIHeP/8iIduw8C4LM37qYg5xwGR2cA7v7rJ7h7+jVM/Ae3sObreUizmX4jpzJywgNWy5Pjd7P26/mknzrGtIffImzAuIplSxY8QOrxA7Tr2pe7n/64QeKrLv7AFlZ9OR9pNjFg9FTG3Godb9LRPaz+cj5nTx3jz48toPdALd7s86f58t0nMZtNmExGht14J4Ov+9NViRngyVmdGdLPj5JSE/Pei+fY8ZrnzluvhuPn64heLzgQm8vbHydgNlcu//PkEB6d0Zmb79xGbp7xqsV+UddYJd6gRyOEeEIIcUQIsfQiy/sLId63/D1dCPGfhozHnswmE0sXvsHTL3/Aa+//wM6t60g7lWSVpn2nbry84CvmvPs9/Ydez/Iv3qtYNm7SPcx86rWGjdFsYuOyuUx+eDHT/7GGo3tjyDyTaJXm8PZlOLt6cv/sn+k7ZjpbVi6wWr7px/l06DnCal6vQbdx2yOLGzT2C8I7OxDgq+fFj7L5Ym0Bd423/fa2A8fKeP2znBrzA3x0RA115V9f5DJ7YQ7f/lzY0CFfUuqSH9k1YWajxmA2m1j71VzufHoRj/4zhsM715Bx2rpc/LFlOc5unjz5r58YfOO9/LLsLW3+b8sAeOS11dz97Kf89N0bmKt8Y982600enhPNw3OiG6wCN5tNrP7yNe55ZiGPz1vNQRvxe/m24baZ8wkffHON9YdHzWDKrDcaJDZbzGYT0Uv+yYzn/o9n/r2aAzvWkl4tXm+/1tz+4DwihlrH6+Hdikdmf81T81bw2Jxv2bR6MXnZGVcl7sH9fGnbxpU/PbiLNz88xrMPh9pM9/IbcUx/Yi93P7oHby8HxgxrVbEswN+J/hE+nM0ouSoxXwkpRJ0+TVVDX5I8AkRJKe+0tVBKuUdK+URdNiyE0NcrsnpKSjhMQOsQWgWFYHBwYODwcezbtckqTffwATg5uQDQqWs42ZmVJ1/P3oNwdnFr0BjPphzE27893v5t0Rsc6d7vZo4f2mCV5vihjfQcNBmArhHjOHlsO1Jqr1pMPPALXv4h+LW2PnlDugzA2dWrQWO/IKKrI9sPal8ASWlGXJ0FXu41T6ikNCO5BTVfETky0plf9xZTVKItyy9q3NdIZm3dQ3lWbqPGcDrpIL4B7fANaIvB4EjYoCji91uXi/h9G4gYOgmAnv3HkXREKxfn0o7TsecQANw9/XB29SQt+fBVjT816SB+gZXxhw+K4si+jVZpfFoFE9S2Gzobra7OPYfg5Nyw515Vp44fwi+wHX6WePsMvom4vdbx+rYKpnW7bohq8RoMjhgcHAEwlpdjlmaulhGD/Vi38SwAsfH5uLsZ8PNxrJGuqFjrGdPrBQ4GHbLKKfb4zM589FmS1bzGJoWuTp+mqsEiE0J8DHQCVgkh/i6E+F0Isc/ybzdLmtFCiBr9sUKIz4UQU6tMF1RJ/6sQ4mvgkGXeXUKIXUKI/UKI/xNC6C2fz4UQh4UQh4QQT9v7+HKyzuHrH1Qx7eMXQE7mxa+Qt/4STVjfq/t+6oKcdDx8KmN09w4kPyfdOk1uOh7erQHQ6Q04uXhQUphNeWkRu39ZxJCbHruqMVfn7aEnK6/yiys7z4y3x5VfvwX66gn01fP8PV68MN2LXp0cGiLMZiUvJx1P39YV054+QeRlp1dLk1GRRq834OziQVFBDoFtuxG/bwMmk5Hsc6mkJceSl3WmYr2Vn77IR7Mn8duq/1ZcDNo9/uwMvHwry7WXTyD51eJvSnKz0/GuGq9vELm1aE3nZJ7hnRcmMf/JsYyeMBNPn4CGCLMGfz8nMs6XVkxnZJbi71ezEgd4a044MV8NoajYyKbfzwEwbKAf5zNLSUxu3N6vGoSo26eJarBKXEr5EJAGjAE+AkZKKSOBV4B59dj0QOAfUsqeQogewB3AMCllBGAC7gQigGApZZiUMhz4zNaGhBCzhBB7hBB7Vn3/aa2CsPkFdZH/6O2b1pB8PI7xk+6p1T7qr2aMonqMFzmO39d+QN8x9+LodPVaLLbYzNJaVA46nSDAV8+bX+WyaEU+997sjotT0z0hrwqb/+WXLxdCQOSIKXj6BLFw7lTWfTOPtl0i0em1oTVTZi3gkddWM+P5r0hJ2MOB31c2RPQX+f9vwv+ntvKyFqt7+7Xm6fnRPPfWOvZuWUl+7nn7xXYJNmO8yKn319mHmHjPdhwcdPTt7YOTk457b2/H4qXJDRhh3TRUS1wIMV4IES+ESBRCPH+JdFOFEFII0d8ex3O1BrZ5AUuEEKFoxaA+zaFdUsoTlr+vA/oBuy1fQi5ABrAa6CSE+ABYA/xka0NSyoXAQoCtcYW1ajb4+AWQdf5sxXR2Zgbevq1qpIs7sJM1yz/huX8uxsHB9lVsQ3H3DiI/uzLGgpx03L0CaqbJOYOHTxBmk5HS4nycXb05m3yAhP3r2bJyAaXFeSB06A1ORI66q8HjHtPPmRGR2uCo5DQjvp6VJ5CPp46cgivvUszON5F02ojJDOdzzaRnmgj01ZN8pgkMsGkknj6BVq3nvOyzeHgH2Ezj5RuEyWSkpDgfFzdvhBCM//MLFekWv/4nfAPaV6wD4OTiTvigCZw+cZCIYZPsH79vILlZleU6Nzsdj6vUOq0LL98gcqrGm3W2Tq1pT58AAoM7cyJ+b8XAN3u7LaoNt4zTemCOJOQT4O9UsSzAz4nzWWUXXbesXLJ1ZyYjBvmRlV1G60BnPn9fq6da+Tvx6bv9eOCZP8jKKW+Q2K9UQzwnbrm9+yFwA5CKVietklLGVUvnATwB7LTXvq9WR/9rwK9SyjDgFsD5MumNWGITWu1ctfar2jcjgCVSygjLp5uU8lUpZTbQB9gEPArYfRRWx9BepJ85xbn00xjLy9m1dT0RA0ZZpUlJOsoXH73O4y++i6e3r71DuKygduHknEsm9/wpTMYyju5dQ6fwsVZpOoePJW7nCgCO7V9Pu66DEUJwx9NfM3PORmbO2Ujk6HsZdOODV6UCB/h1bwlzF+cwd3EO+46VMqS3Vlw6tTFQXCpt3vu+mH3xZXRvr10zursIAv30nMupObq9JWnTMZzM9BSyz6ViNJZxeOdaukVYl4tuEWPZ/3s0AHF71tOxu1YuykqLKSstAuB47DZ0egMBwV0wmYwU5mcDYDKWc+zAJgKCuzZI/MHV4j+0cy3dI8c0yL7sIaRTGJlnU8jK0OI9sON/9Oh7ZfHmZJ6lvEwbE1JUmEtKwj5ate7YYLH+uDaN+57cy31P7mXLjvOMH6vdBujVzYOCIiOZ2daVuIuzruI+uV4HQ/r7kpJaRFJKIbfcvZ1pM3cybeZOzp0vZcZTexu9AocGa4kPBBKllElSyjLgW2CijXSvAf8G7DbS72q2xE9b/p5+BemT0VrY36NlxMVa7huAlUKId6SUGUIIX8ADraIvk1L+IIQ4Dnxe99Bt0+sN3PnA33lnzqOYzWaGX3crwe06E/31R3To0pOIgaNYtuRdSkuK+OjN5wDwbRXEEy++C8C/XpzBmdPJlJYU8+zM8Ux/9BXCIofaNUad3sCYaa/ww39nIqWJsMFT8G8dyrY17xHULozO4dcRNmQq//vib3wy5wacXb24+b53LrvdNZ89Q2riLooLsln48kiGRD1O+JBpdo39gkOJ5YR3dmTeIz6UlUs+i6l8xOWVmd7MXayNSJ861pWBvZxwdIB/P+7D1v2lrNpSRGxSOb06OTJ3ljdmCcs2FFJY3HijbCK+fAu/UQNx9Pdh7InfSJj7Aac+W35VY9DrDUTd9TJfvn0/0mwmcvgUAoJD2bjifdp0CKN75FgiR05lxaLneO/5G3Fx82Lqg28DUJifyVdvzUTodHh4B3LbTG2Ut8lYxldv34/JZESazXTqOYR+oxqmTOj1Bibc9RJLFszEbDbTd8RtBAaHsuHHOaFO8wAAIABJREFU92nTMYwekWP/n737Do+iWh84/j276b2RAiQQQqgJhI70IoKAgAKKvVwvYsN7lYvtXgsq6BX7/VlAQRBsiCBNiiBNQDqBEEgIBBJKEtJ7srvn98csSTYJkLIxCTmf59mH7MzZmXeGM/POOdNIPH2U7z55mvzcLE4c/p0tKz5h+mzt8psvZ99HysXTFBXk8e4/hzDhkTcJDR9QJ7FeiXf8gy/z1X//jslkotfg2/FvGcrGnz6hZXBnOvUYRkLcURZ/OJ38vCyiD/3OpuX/47l3VpN84TRrv/0vQgiklAwa/TABgXVzcFTe7v1p3NTTix/m9S65xeyKhR/14OFnDuDgoOft/3TG1kaHXi84cCSDX3698JfEV2N1c367BZBQ5nsi0MdytqIbECilXCOEmGGtGYu6uvgEQAgRD/QEQoFFQAqwBbhfStlaCDEEmCGlHCuEeAjoKaV8SgjhB/yC1hrfDDwtpXQpW77MPO4CXjSXLUZreeejnQe/cvj0opTy12vFWt3u9PoWlVi/56qra9++v+Y8njXd/tpfeyGiNWRtPVHfIVSLXteoNjsA7GwaX8xzZ+2s7xCqbefqwXWSbZOP76/Rf6Bf516PAWUfqDDPfEoWIcRkYKSU8lHz9/uB3lLKp83fdWi57yEpZbwQYitaLttf8yXR1GlLXErZ2vznZaDs4eN/zOO3onV5I6X8GnOLWUqZBPQtU/7F8uXLzOMH4IdKZt+9FqEriqIoN6Ca3vNd9hqqSiQCgWW+t0S7sPsKVyAM2Gq+fssf7c6tcbVN5OqJbYqiKEqTUUf3fO8DQoUQwWinjqcA95TMU8pMwOfKd2u2xBvuHeyKoiiKYmUSUaPPNacppQF4CtgARAM/SimjhBCzhBDj6nJ5VEtcURRFaTLq6ulrUsp1wLpyw165Stkh1pqvSuKKoihKk9GQn4NeEyqJK4qiKE1GXTzspT6pc+KKoiiK0kiplriiKIrSZDTkN5LVhEriiqIoSpNxo3WnqySuKIqiNBmqJa4oiqIojZRqiSuKoihKI6Va4jeo/aec6juEajEYqv5O7YbA0fmvfZe6NTS2l4kAuA3pUN8hVEvr6K31HUK1bT8VUN8hVNtd0wbVdwgNhmqJK4qiKEojpR72oiiKoiiNlJQqiSuKoihKoyRvsGecqSSuKIqiNBnqnLiiKIqiNFIqiSuKoihKI6WSuKIoiqI0UiqJK4qiKEojpa5OVxRFUZRGSrXEFUVRFKWRutGS+I11w5yiKIqiNCGqJa4oiqI0GTdaS1wl8es4d2IHO1e9hTSZ6Nh7Et2HTbUYbzQUsfn750lJjMLByYMR972Pm1dLAA5u+YLovcsROh0Dxr9MUPuBpCefZtOSZ0t+n5WWQK+R0+k68EEun49m28+vYSwuRKfXM/D2V/EL6lKr+KWU7F49m4ST27Gxc2DwpNn4tOhcoVzK+Si2LXsRY3Ehge0HcdNtLyGE4PTR9Rz47X9kpJxmwhM/0qxlGACJsX+wb/37GI3F6PW29B79L1qE9K1VrFczcbA9nYNtKSqWLNmYT2JKxZe/jO1nT++OtjjZC2Z8ml0yfGg3O24Ks8Vkgpx8ydJN+aRnS6vGF3t0B+u/fQuTNNF94CQGjrGsI4biIlZ8+TwXzkbh5OzBpMffx9OnJQZDEWsWvcqF+GMIoWPUPS8R3KEPAAvfuZ+cjBRs7BwAuP+5r3Bx87Zq3FXVZf5sfEcPoSg5le3dbquXGMo7uP9PFsz7HyaTkZtvGcMdd95rMX7Vih/5bcNa9Ho9bu4ePPmPmfj6+gOweMEXHNi/G4DJUx5gwKBhdRJjfPR2tv38FiaTibC+k+k1oly9MBSxYclMkhOicHD2YPSDH+Du3ZJLZyP57Yf/aIWkpO+op2nbdQTZ6RfZsGQmudmXEUJH+E130m3Ig1aN+Wz0Dnas1PZ3nfpOosfwivu7Td8+T4o55pEPaPu7/Nx01n/9DMkJx+jQawKDJ75S8puYg2vY/9sXCCFwdvNlxL3v4ujiadW4q+NGu7DNKt3pQojpQohoIcTSWk7HQwjxRJnvzYUQP9U+wpoxmYzsWDGLsX+bz5QZazh1eC1pSacsykTv/Ql7RzfufWEjXQY9yJ517wGQlnSKU4fXMWXGGsY++iU7fp6FyWTE07cNdz67kjufXcmkfyzHxtaRNmE3A7B77bv0HPEkdz67kl63TGfP2ndrvQwJJ7eTmXqWO2esZ8Dtr7Nz5axKy/2x8nUG3v46d85YT2bqWRJjdgDg6RfKiPs+IaB1T4vyDs6e3PLgZ0z6xyoGT57D1h+fr3WslenU2gZfTz2zvs7h+80F3DXcsdJyx04bmPtdboXhiSlG3v0ul7eX5nL4VDETBjpYNT6Tyci6JbO495/zefLNNRz7cy3J5y3ryMEdP+Hg7MYzb2+k7y0P8tsyrY4c3LYMgCfeWM39Mxaw8Yd3MJlKD1DumPouj7++ksdfX1lvCRwgcdHP7B37aL3Nvzyj0cj8zz7i36+/w0efLWLH9i0knIu3KBPcJpR3P/yCD/5vATf1H8ziBV8AsH/vbk7HxfD+J1/yzvuf8cvy78nLq1hvastkMvL7sllMeOxLHnhxLScPriH1kmW9iNq9DAdHNx7+zya6D3mInavnAuAdEMo9zy3nvpm/cPu0L9n84yuYjAZ0Oj2DJrzAgy/9ypR//sCRnd9WmGZtY9728yxumzqfe55fQ8zBtaSVm/7xP7X93f0vb6Tr4AfZtUaryzY29vS59Rn6j5tpOU2jgR0rZ3P7E4u5+1+r8G7ensidS6wWc02YEDX6NFTWOif+BDBaSllyOCyEqEkr38M8LQCklBeklJOsEF+NJJ+LxN0nCDfvQPQ2drSNGE181GaLMvFRm2nfYwIAIeEjOR+7Gykl8VGbaRsxGr2NHW5eLXH3CSL5XKTFb8/H7sbdOxBXzxYACCEoLsgBoKggGyc331ovw9noLYR2G48QAr+gCIoKssjLSrYok5eVTFFhDn6tuiGEILTbeOKPa8vp6RuCR7PgCtP1ad4JZ3N8nn6hGIsLMRqKah1veeEhNuyN1qYbf8mIox24OVXcoOIvGcnKq9jCjk00Umwwl7loxMPFuhvj+dORePkG4eUbiI2NHWF9RnPysGUdOXloMxH9tDrSqedITkdrdSTlQhzBnW4CwMXNGwcnNy7EH7NqfNaQtnM/xWmZ9R1GiVMxJwho3gL/gObY2toyYNAw9u75w6JMeNdu2DtoB2ztOnQi9XIKAIkJZ+kc3hW93gYHB0daB7fl0IG9Vo/x0tlI3Ju1wt1H23e06z6GuKOW9SLu2BY69r4dgNCuI0mI0eqFrZ0jOr22+zQYChHmBOLs7otvoNaLZufggpdfG3IykqwWc5J5f+du3t+FdhvN6WOWMZ8+tpkOvbS63LbLSBLN+ztbeyeat+mB3sbylcMSiZSS4qI8pJQUFeTg7F77/VptSESNPg1VrZO4EOJzoA2wSgiRKYSYJ4TYCCwWQuiFEO8KIfYJISKFEI+V+d2/ygx/3Tz4bSBECHHY/LvWQohj5vIPCSFWCiFWCyHOCCGeEkI8K4Q4JITYI4TwMpcLEUKsF0IcEELsEELU+AXLuVlJOHuUvjvY2d2f3EzLjSYnMxkXcxmd3gY7B1cK8jLIzUzCxb3cb7Msf3vqyDradhtT8r3/uJfYvfZdFr85hN1r/kvf0c9SW7mZSbh4+JeLwzKJ52Yl4+zmV6aMX4XlvJYzxzbi3bxjhQ3YGjychUX3d0aOxL2GifimznYcjzdYKzQAsjKScPMq/X928/QnKz2pXJnkkjJ6vQ0Ojq7k5WTgF9iek4c2YzQaSE9J5EJ8FFlpF0t+98uCl/js1QlsW/UpUlr3FEBjlpqagrdPs5Lv3j7NSEtNuWr5zRvX0r1nbwBaB4dwcP9eCgsKyMrM4FjkIS6nJF/1tzWVm5mEa5ntztWj4jaVm5GEq2fpvsPewZWC3HQALsYfYfGcMSx5exzD7ny9JKlfkZmaSEpiNP6tu1o55tK67OJRcX+Xm5lcUqZkf5ebcdVp6vW2DJn0Kt+9O46Frw0iPSmOTn3qrV0GaN3pNfk0VLU+Jy6lnCaEGAUMBZ4CbgMGSCnzhRBTgUwpZS8hhD3whznBh5o/vQGBdgAwCHgBCJNSRgAIIVqXm10Y0A1wAE4Bz0spuwkhPgAeAD4E5gHTpJSxQog+wKdApSe9zPFNBZj8xOf0G2l5/ofK9psV3kVbsZAAKt/nlv7WaCgiPmoLfW4tTdRRu7+j320vENJlJKeO/MrvP/6bcY8trGxC1VBJIOWXoZJgRRXfuZuWFMve9e8x+pEvaxLcdVnr1b89O9gS6Kfj458KrDPBKypdvVVZv9Bt4EQuXzzNvFmT8PBuTmDbbiU764lT5+Lm6Udhfg4/fDqdI7t+IaL/BOvG3lhdZ9sqa9uWjZyKPcmb73wEQET3XpyKOcGLM57Ezd2Ddh07o9frrR9ipTsAyxjlNbbNgNZdeeDFtaRdimPD0udp3WkQNrb2ABQV5rJ2wXQG3/ES9g4uVgy6spCvX5ev1Ug1Gos5tut7pjy3AjfvQLb//AYHNs+j14jHaxVqbTTkVnVN1MWFbauklPnmv28Bugghrhx6uaMl71vMn0Pm4S7m4eeuM+3fpZTZQLYQIhNYbR5+1DwfF6AfsKzMjtT+ahOTUs5DS/p8uKpi7XR29yM3o7RllJt5qaQL+QoXdz9yMi7i4uGPyWigqCAbeycPXDz8yMm8+m/PndiBT4tOOLn6lAw7eWAl/ce/DEBIl1FsXfbv66yOykXtXsqJfdqlBM1ahpGTcckyDtdmFuWd3f0seglyM5Oq1JWfk3mJTd88zZDJb+PmHVSjWCszsIst/cK1Vv25S0Y8XUs3Og8XQWZO9Vql7QP1jOxtx0fL8jAYrRYmAG6efhat56z0S7h6+FZaxt3LH6PRQEF+No7OHgghGHX3iyXlvnxrCl6+rUp+A2Dv6EJ4n7GcPxOpkriZt0+zku5xgNTLKXh5+1Qod+TQfn76YQlvvPMRtralvUSTptzPpCn3A/DBf98goHlLq8fo4uFPdpntLjsjqUI3souHP9npF3E17zsKC7JxcPKwKOPlH4KtnSOpF2PwCwrHaCxmzYLpdOh5G2273mLVmJ09/Mgus7/Lyai4v7tSpuz+rnzMZV0+fwIAdx9t/9A24lYObp5v1birqyG3qmuiLu4TL3uViACellJGmD/BUsqN5uFzygxvK6X8qgrTLizzt6nMdxPaAYkOyCgz3QgpZceaLohvYDgZl8+SlZaI0VDEqcPraN3JslHfutMwTh5YCUDc0Q20aNsXIQStOw3j1OF1GA1FZKUlknH5LL5lrjQ/dXgtoWW60gGc3Hy5cFo7P3f+1B7cfVrVKO7ON93LxOkrmDh9Ba07DSf20C9IKUk6dxg7B9cKCdrJzRdbO2eSzh1GSknsoV9o1fHaV+wW5mex4etp9B71LP6tu9cozqvZEVnMO0tzeWdpLpFxBnp31HbArf31FBRR6bnvq2nZTMddwx2ZtyqfnHzrd0k3Dw4nNeks6SmJGAxFHPtzHe0jLNdd+4hhHN6l1ZHj+zcQ3EGrI0WF+RQV5gEQF/UHOr0Nvi3aYjQayM3WulWNhmJijmzFt0U7q8feWLVt156L5xNJunSR4uJidm7fQq8+/SzKnI6L5fP/vc+Lr8zGw6P0Smij0Uh2lnZ+P/5MHPHxcUR0t7xo0xr8g8LJSIknMzUBo6GImINrCQmzrBchYcOI3rsCgNgjGwgM1epFZmoCJqN22icr7TzpyWdw82qBlJLfvnsZL782dB/6sNVj9gsMJzPlLFmp2v4u9tA6gsvFHNx5GCf2aXX5VOQGWpr3d1fj7O5L2qU48nPSAEiI2YWnXxurx14dN9o5cWGNc21CiHigJ1p3eo6Ucq55+FRgNDBZSlkshGgHnAf6A28Aw6WUOUKIFkAxYAQOSilbmX/fGlgjpQwTQjwE9JRSPlV2nlLKy2XHCSF2AR9IKZcJrXZ1kVIeud4yVNYSBzgbvY0/Vs1Gmkx06D2RHsOnsXfDxzRrGUZw52EYigvZ/P1MLp+PxsHJnRH3vo+bdyAABzZ/zom9yxF6Pf3HvUSrDoMAKC7K55u3hnDvC79h7+haMq+LZw6w85e3kCYjeht7Bt3xSsktXeUZDFX7f5NSsmvVGyTE7MTGVrvF7Mo0l398OxOnazuRlMRjbPvpRQzFhQS2G0i/cf9GCMGZqE3sXvUW+blp2Du64RXQgdGPfMnBLZ9xZOt83MocaIx+5EscXSq/ivrsuZwqxVuZyUMd6NjKhmKDdotZQrJ2Bffz9zrzzlLtmHH8AHt6tLfF3dxS3x1VzK97CnnqDicCvHUliT89y8S81flXnVdZ/Xq5Xr8QEBO5jfXfaXWk24CJDLptGltWfEzz1mF06DaM4uJCVsyfycVz0Tg6uzPpsffx8g0k/XIiS957FKHT4erhx/iH38TDpwVFhXksfPs+jEYD0mSiTaebGDnlBXS663f7ug2p8SUgVxXxzXt4D+6NnY8nhUmpxM76hISF1rlppHX01hr97sC+PeZbzEwMH3Erk6bcz3ffLCAktD29+/bntZee5ezZM3h6egHg08yPl16dTVFRITOma6fNHJ2cmPbkswSHhFZr3ttPBVy/EHAmahvbVsxGmox07juR3rc8zu51H+EbGEZI+HAMxYVsWPIvkhO1fcfoBz/A3SeQ6H0r2ffbfHR6G4TQ0Wfkk7TtcjPn4/az7ON78QloBzqt/dV/zLMEdx583VgMxqrtL+KPb2PHL1pd7tR7Ij1HTOPPXz/GNzCM4DBtf7fp25lcTozG3smdkQ+8j7t5f7fojWEUFeRiMhZj5+jK+Me+wsu/Lcd2fc+R7YvR6W1w9WzO8Lvn4Oh8/VvMnh5jrZNplvaeyKxR0uvdwb1BZvK6TuI64E208+QCSAEmSCkzhRDPAFfuW8kB7pNSxgkhvgW6AL8C/0f1k3gw8BkQANgC30spK7+vqoyrJfGGqqpJvKGoTRKvL1VN4g1JXSTxulTTJF6fqprEG5KqJvGGpK6S+J4aJvG+N3ISvxGoJF63VBL/a6gkXvdUEv9r1FUS3x2dVaOVcVNHtwaZxNUT2xRFUZQmoyGf364J9QIURVEUpcmoq/vEhRCjhBAnhRCnhBAvVDL+WSHEcfOzUTYLIWp25XI5KokriqIoTUZdXJ0uhNCjXcN1K9AJuFsI0alcsUNo1251AX4C/muN5VFJXFEURWkyTLJmn+voDZySUp6WUhYB3wPjyxaQUv4upcwzf90DWOUBBSqJK4qiKE1GTVviQoipQoj9ZT5lH/HZAkgo8z3RPOxq/oZ2B1atqQvbFEVRFOU6yj7hsxKV9bdX/oBgIe5DuyX7+jf4V4FK4oqiKEqTUUePXU0EAst8bwlcKF9ICHEz8DIwWEpZWH58TagkriiKojQZdfREkH1AqPlhY+eBKcA9ZQsIIboBXwCjpJRWe3WeSuKKoihKk2Gqg/vEpZQGIcRTwAZADyyQUkYJIWYB+6WUq4B30V72deUFXeeklONqO2+VxBVFUZQmo67eYialXAesKzfslTJ/31wX81VJXFEURWkyGtcDtq9PJXGzln6N6382Pbtx3R3o5eVY3yFUm17XuOoENL5nkcd3HFLfIVSb/YaT9R1CtR2PzK7vEGrArU6meqM9dlUlcUVRFKXJqMKDWxoVlcQVRVGUJqOuzonXF5XEFUVRlCZDnRNXFEVRlEaqLm4xq08qiSuKoihNhmqJK4qiKEojpc6JK4qiKEojpa5OVxRFUZRGSnWnK4qiKEojpR72oiiKoiiNlOpOVxRFUZRG6kbrTm9cD+BWFEVRFKWEaonXQkzkDtYumY3JZKLn4EkMvu3vFuPPnNjH2qVzSEqI4a4n3iOs98iScV+/+3cS4o7QKrQ7Dzz3eZ3FeCZqO1t+egtpMhHefzJ9bplqMd5QXMSvi2eSdC4KB2cPbvvbB7h7tywZn5V2gYVvjKHfmKfodfPfADjw+yIi/1gGUtKl/2R6DHvI6nHf2ktHaAsdxUZY+YeBi2kVywR4we39bbDRQ+x5E7/uMwEwpKuOHqE6cgu0cpsPGYk9L/FwhqfG23A5SxuemGJizZ8mq8YdG7mDtd/ORppM9Bg0iUFjLetE/Ml9rPtWqxOTH3+PsF6ldWLR3L+TGHeEoHbduf+fdVcnyju4/08WzPsfJpORm28Zwx133msxftWKH/ltw1r0ej1u7h48+Y+Z+Pr6A7B4wRcc2L8bgMlTHmDAoGF/WdxX02X+bHxHD6EoOZXt3W6rtzhOR21n849vYZImuvafTN+RFbe9tYtmculcFI7OHox/VNv2MlMT+fL10Xj5BQPQPLgrI++ZBYDRUMSmH97gXMxehBAMGvdP2ncfWWHe1jJxsD2dg20pKpYs2ZhPYkrF7WVsP3t6d7TFyV4w49PSF60M7WbHTWG2mEyQky9Zuimf9Oz6bwbfaC3xGzqJCyEigObm97xalclkZPXiN3h45le4efnx2at30rH7UHxbtC0p4+HdnEl/n8OOXxdU+P3A0Y9QVFTAvi0/WDs0ixh/+3EWk59eiKuHH0v+O4mQ8GH4BJTGeHT3Mhyc3Hj09U2c2L+W7SvnctvfPiwZ//vyOQR3HljyPeVCDJF/LOO+mcvQ62356f8epU3YEDx9W1st7tAWAm83wccrDbT0EYzto2f+r8YK5cb21bNqt5HEy5L7hutp21xw6oK2he4+bmLX8Yo7nLRs+HyNwWqxlmUyGVn9zRs89C+tTnz++p106GZZJ9y9mnPHo3PYWUmdGDD6EYoLC9i3te7qRHlGo5H5n33Eq2/OxdunGTP/OY1effsTGNS6pExwm1De/fAL7B0cWL/2FxYv+IIZL7zK/r27OR0Xw/uffElxcTH/ef4Zuvfsg5OT818Wf2USF/1M/KdLiFjwTr3FYDIZ2fT9LO6avhBXTz8WvT2Jtl0st73IXdq299isTRzft5atK+Yy/lFt2/PwCeLhl3+pMN1dv36Ok4sXU1/fgDSZyM/LqLNl6NTaBl9PPbO+zqG1v567hjvy3ve5FcodO21g++EiXnnIxWJ4YoqRd78rotgAA7rYMmGgAwvX5ddZvFVlusHuE7/Ru9MjgNF1MeHEuEi8fIPw8g3ExsaOLn1HE31wi0UZz2Yt8A9qjxAVV3NI55uwd6jbnd2l+Eg8m7XCwycQvY0dHXqMIS5ys0WZuMgtdO5zOwDtuo3k3MndSPOhauyR33D3bol3QGhJ+bRLcTQP7oqtnSM6vQ2Bob2IPbLJqnF3CBQcjtMScOJliYOdwKXcm0xdHMHeVpB4WYv1cJyJjkH1u3Emno7E26+0ToT3GU30oUrqRGB7dJXViU51XyfKOxVzgoDmLfAPaI6trS0DBg1j754/LMqEd+2GvYMDAO06dCL1cgoAiQln6RzeFb3eBgcHR1oHt+XQgb1/afyVSdu5n+K0zHqN4WJ8JB7NWuHRTNv2OvYcQ+wRy20v9sgWwvpq216H7iM5e6J027uao7uX03fUYwAInQ4nF6+6WQAgPMSGvdFFAMRfMuJoB25OFbex+EtGsvIqxh2baKTYfLwcf9GIh0vDSJ5S1uzTUNV7EhdC/EcIcUIIsUkI8Z0QYoYQIkIIsUcIESmEWCGE8DSXvdrwrUKInua/fYQQ8UIIO2AWcJcQ4rAQ4i5rxp2Vnoy7t3/JdzcvPzLTk6w5i1rLzkjC1bM0RhcPP7IzkiopEwCATm+DnaMr+bnpFBXmsXfTfPqNfsqivE/zdiSe2k9+TjrFRfmcjtpOdvolq8bt6iTIyiv9npUnK+w83JyExY4jK0/73RW9O+h4/DYbxvfT42BX+jtPF5g21oaHb9ET5GvdnUpWejLuXqXr293Tj+wGVifKS01NwdunWcl3b59mpKWmXLX85o1r6d6zNwCtg0M4uH8vhQUFZGVmcCzyEJdTkus85sYgOyMJtzLbnqunHznltr2cctuevXnbA8hMTWThWxP49v37SIjdD0BBnnYeaMfqj/h69u2snD+d3KzLdbYMHs7Covs7I0fiXsNEfFNnO47H100PWHWpJG5F5sQ7EegG3AH0NI9aDDwvpewCHAVevc7wCqSURcArwA9SyggpZYU+SiHEVCHEfiHE/k0r51UrdknF/1XR4O4/rCRGUS7GSmqnQLBr7Sf0GPogduVaht7+IfQe8SjL/vcIy//3KL4t2qPT6a0adWVr8XotFK2Q9s++kyY+WmHg89UGcvIkI3tq8WXnw/s/G/h8jYH1+41MGqjH3tZ6cVe+pTe0OlFOpau18pi3bdnIqdiTTJg4BYCI7r3o0bMPL854kvf/+wbtOnZGr7duXWi0KqsL5ba9q+1DnN18efyt33n45ZUMm/gCqxc+R2F+DiaTgez0S7Rs052HXlpB8+Bu/L687k4ZlN9V1FTPDrYE+unYfKDIOhOsJZOs2aehqu9z4gOAX6SU+QBCiNWAM+AhpdxmLrMIWCaEcK9seG1mLqWcB8wD+OnP6v03uXv6kZla2gLNSkvCzdO3NuFYnauHv0UrOScjCRd3yxhdPf3JTr+Iq6c/JqOBovxsHJw9uBh/hJhDG9i+ci6F+VkIoUNvY0/3IfcR3m8y4f0mA7Djl/dx8fSrday92+voHqodU15Ilbg5lY5zcxJklzuVVr517uYE2fnaf+GVC9oADsSauGeYVs2NJsgv1IZfTIO0bIm3m+BCqnW2UDcvPzLTStd3ZnoSrg2sTpTn7dOspHscIPVyCl7ePhXKHTm0n59+WMIb73yErW1p18akKfczacr9AHzw3zcIaN6ywm+bIldPf7LKbHvZ6ZVsex7atudm3vYKzdueEAIb8zr2bxWGh08Qacln8A8Kw9bOkXYRIwCnMkaXAAAgAElEQVTo0H0Ukbt+smrcA7vY0i9cm/e5S0Y8XUu3MQ8XQWZO9baV9oF6Rva246NleRgqXtZSL260Z6fXd3e6tdamgdJlcbDSNK+pRZtwUpPOkpaSiMFQROSedXToNvSvmHWV+bcKJz05nozLCRgNRZw4sJaQcMurh0PChxH15woAYg5tILBdX4QQ3P3st0x9YwtT39hC96EP0mfkY3Qfch8AudmpgHbleuyRjXTsObbWse49aeLzNVorOfqciYgQ7b+zpY+goFiSUy6J5+RDUbGkpY9WhSJCdJxI0HYwZc+fdwzSkZyhDXeyL21deLqAt5uw6tWyLYK1OpFurhNH/2x4daK8tu3ac/F8IkmXLlJcXMzO7Vvo1aefRZnTcbF8/r/3efGV2Xh4eJYMNxqNZGdp557jz8QRHx9HRPeeKBBQbtuL3r+Wtl0st73QLsM4tkfb9k4c3EBQe23by8tOw2TSMl5GSgLpyfF4+AQihCAkfCjnYv4E4OzJ3fgEhFg17h2RxbyzNJd3luYSGWegd0ctobf211NQRKXnvq+mZTMddw13ZN6qfHLyG05T9kbrThdV6qasq5kL0Qv4AuiH1itwAJgP3A88JaXcIYR4DXCXUv5TCHHkKsO/BA5IKT8TQvwD+IeUsrUQYiIwTkr54PViqW5LHODkkW2sXTIHKU10H3QHQ8dN47flH9MiOIyO3YeRePooSz96mvzcLGxs7XD18OGZOWsAmPfmfaRcPE1RQR5OLh7c8bc3Ce0yoMrzTs+u2vHX6WPb+H35bEwmI+E3TaTvqMfZueYj/IPCaNtlOIbiQtYt+hfJCdE4OLsz9pEP8PAJtJjGH2s/wc7eqeQWs+/ev4f83Az0ehuG3PEirTrcdN04Ei8UV3nZAMb01tG2hY5iA6zcZSxpLU8ba1NydXlzb8GEfnpsbbRbzNbt1S6Gu6O/Hn8vgUQ7j7d6j5GcfOgYJBgWocdk0rrHfj9iJCbx6v/tnUOr3zUcc2Qb676dg8lkovvAOxgybhqbf/6Y5sFhdOym1YnvPimtEy7uPkyfrdWJL2db1okJj7xJaHjV6wRA52bVPwd/YN8e8y1mJoaPuJVJU+7nu28WEBLant59+/PaS89y9uwZPD21i6h8mvnx0quzKSoqZMZ07bYpRycnpj35LMEhodeaVQXxHYdUO97rifjmPbwH98bOx5PCpFRiZ31CwkLrtViTNpysUrm4Y9vYvGw20mQkvN9E+t36ODtWa9teaFdt21vz9b9ISojG0cmdcX/7AI9mgZw8uIEdaz5Gp9Oj0+kZMPbpkgOAzNTzrPl6JoX5WTi5eDH6gTm4eTW/biyHIrNqtKyThzrQsZUNxQbtFrOEZG0be/5eZ95Zql2pPn6APT3a2+Jubqnvjirm1z2FPHWHEwHeupLEn55lYt7qql+d/sk/3Oqkyfz11spPIl3PQ0Ma5rmxek3iAOZkfDdwFkgBtgL7gM8BJ+A08LCUMt18y1hlwzsAPwI5wBbgPnMS9wI2ALbAnMrOi19RkyRen6qaxBuK6ibxhqAmSby+1SSJ16e6SOJ1rapJvCGpaRKvT3WVxBf+XrMk/vDQhpnE6/ucOMBcKeVrQggnYDvwnpTyMNC3fMFrDD8BdCkz6N/m4WlArzqJWlEURWl0GnLXeE00hCQ+TwjRCe1c9iIp5cH6DkhRFEW5MTWuPtfrq/ckLqW8p75jUBRFUZoG1RJXFEVRlEbKZN3XJdQ7lcQVRVGUJkO1xBVFURSlkVJJXFEURVEaqRvtwrbGdbOxoiiKoiglVEtcURRFaTJq/oCzBvmsF9USVxRFUZqOunp2uhBilBDipBDilBDihUrG2wshfjCP/1MI0doay6OSuKIoitJkmEw1+1yLEEIP/B9wK9AJuNv8ELOy/gakSynbAh8AVnmPrEriiqIoSpNRRy3x3sApKeVpKWUR8D0wvlyZ8Wiv0Ab4CRguRO3f2q7OiZv5u1b97ToNQVyC4/ULNSA2tg3zfNK12Nk0vstYt58KqO8QqsW+Eb5MxG9k+/oOodpClp+o7xAajJpenS6EmApMLTNonpRynvnvFkBCmXGJQJ9ykygpI6U0CCEyAW/gcs0i0qgkriiKojQZNb2uzZyw511ldGWtlPJzqkqZalNJXFEURWkyZI1vFL9mb2IiEFjme0vgwlXKJAohbAB3IK2GwZRQ58QVRVGUJsMka/a5jn1AqBAiWAhhB0wBVpUrswp40Pz3JGCLrPn9biVUS1xRFEVpMurisavmc9xPARsAPbBAShklhJgF7JdSrgK+Ar4RQpxCa4FPsca8VRJXFEVRmgxTHT13VUq5DlhXbtgrZf4uACZbe74qiSuKoihNhnoBiqIoiqI0UiqJK4qiKEojZbrBsrhK4oqiKEqTIa/zCNXGRiVxRVEUpcmwwl1dDYpK4oqiKEqTcb2XmTQ26mEviqIoitJIqZZ4LRw9+AfffTUXaTIy8ObbGT3xYYvxG35Zwo7fVqDX63Fx8+Thp17Fx7c5AB/MepK4k0cJ7RjBM//+uM5ilFLy59rZJJzcjo2tAwMnzsanRecK5S6fj2LH8hcxFBcS2H4Qfca8hBCCvb++S8KJ39HpbXH1CmTgxNnYO7px/tQf7N/wPiZjMTq9Lb1G/YvmIX2tFvfI7jraNhcUG2HVHiOX0iuW8feE8X312Ojh1AXJhoPaIfaQcB3tWgqkhNwCyao/TeTkg70tTLhJh7uTQKeD3dEmjpyxftfaySM7WPXNHKTJSK8hkxg67u8W40+f2M/qb+ZwKSGGu5+aS5feIwFIv3yebz58BpPJiNFooP8t99J3uFWeB1FBfPR2tv38FiaTibC+k+k1YqrFeIOhiA1LZpKcEIWDswejH/wAd++WXDobyW8//EcrJCV9Rz1N264jyE6/yIYlM8nNvowQOsJvupNuQx6sZM41dzpqO5t/fAuTNNG1/2T6jiwXc3ERaxfN5NK5KBydPRj/qBZzZmoiX74+Gi+/YACaB3dl5D2zADAaitj0wxuci9mLEIJB4/5J++4jrRp3VXSZPxvf0UMoSk5le7fb/tJ5nzuxg52r3kKaTHTsPYnuwyzXq9FQxObvnyclMQoHJw9G3Pc+bl4tATi45Qui9y5H6HQMGP8yQe0HArBk9jBs7Z0RQo9Or2fSM8sBuHzhBNuXv0pxUR6uni24+Z652Dm4/KXLq7rTr0IIkSOl/Gv/N+qRyWhk6bx3eO61T/H09uONmfcR0XswzQPblJRp1aY9Q+Yuwd7ekd/XL+OnxR8xbYb2CtmREx6gqLCAbRuW12mciTHbybx8lknPricl4Qi7Vs1i3OM/VCi365fX6T/hdZoFRrBx0WMkxuwgsP0gWrTtR89b/olOb8O+9XOJ3DaPXqNm4ODkyYj7P8PJzZf0pBg2LPw7U17YZpWY2wYIvFzh/9YYaeENo3vqWbDJWKHc6F561uw1cj4V7h6sIyRAEHdRsivaxNajWple7QSDOutYt99Ez1DB5Uz4YbsRJ3t4Yoyeo2eNVu1eM5mMrFz0Jo++8CXuXn7875W76NRjKH4t2paU8fAO4M7HZrN93UKL37p6NOOJV7/FxtaOwoJcPnhhPJ26D8PN09d6AZpj/H3ZLO54YiEuHn58994k2oQPw9u/NMao3ctwcHTj4f9s4uTBtexcPZcxD32Id0Ao9zy3HJ3ehtzMZJb8dzxtwoai0+kZNOEFfAM7U1SQw7dzJxLUob/FNGsb86bvZ3HX9IW4evqx6O1JtO0yDJ+A0ulH7lqGg5Mbj83axPF9a9m6Yi7jH/0QAA+fIB5++ZcK09316+c4uXgx9fUNSJOJ/LwMq8RbXYmLfib+0yVELLDKK6arzGQysmPFLG6bugBndz+WfzyZ1p2H4eVXul6j9/6EvaMb976wkdjDa9mz7j1uue8D0pJOcerwOqbMWENuVjKrv3iYu59fj06nB2DctMU4OntazG/rsn/Tb+xMmof0Jnrvcg5v/Yreo575a5f5xsrhqju9pk7HHsM3oCXN/FtiY2tL7wEjObR3q0WZDuG9sLfXXhnapl046anJJeM6demDg6Nzncd5LnoLbbuNRwiBb1AERQVZ5GUlW5TJy0qmuDAH36BuCCFo220856I3A9AitD86vXas1yywK7lZSQB4N++Ek5uWXDx8QzEaCjEaiqwSc7uWgsh4bUs7nwoOduDiYFnGxUFrWZ9P1b5Hxkvat9ReUFBkKC1nZ2P5miA729Lh+UXWPz+WEHcUb78gvH0DsbGxo2vfWzl+YItFGa9mLQgIao8QlpufjY0dNrZ2ABiKizHV0WW0l85G4t6sFe4+geht7GjXfQxxRzdblIk7toWOvW8HILTrSBJidiOlxNbOsaQ+GAyFCPNLIZzdffEN1Hp47Bxc8PJrQ05GktVivhgfiUezVng002Lu2HMMsUcsY449soWwvlrMHbqP5OyJ3ddtdR3dvZy+ox4DQOh0OLl4WS3m6kjbuZ/itMy/fL7J5yJx9wnCzVtbr20jRhMfZble46M2077HBABCwkdyPlZbr/FRm2kbMRq9jR1uXi1x9wki+VzkNeeXkXKGgDa9AAhs14/TRzfWzYJdgzTJGn0aqholcSHESiHEASFElPkdq1eGvyeEOCiE2CyEaGYeNl0IcVwIESmE+N48zFkIsUAIsU8IcUgIMd48/CEhxM9CiPVCiFghxH/LTHuUedpHhBCbrzOdzkKIvUKIw+b5htZ8FVUuIy0FLx//ku+e3r5kpCZftfzO31YS1r2/tcO4rrysJJzdS+N0dvOvNIk7ufuVlnH3Iy+r4g449sDPtGw3sMLw+KiNeDXviN7GzioxuzpCVm7pRpOVJ3F1KlfGSRtuUabMK9aHdtExfZyesFY6th3VkuG+GImPG/xjgp7HbtWXdL9bU2Z6Eh5epevb3cufzPSr14vyMlIv8sGLE5jzzDCGjH3U6q1wgNzMJFw9SmN09fAjN9Py/zs3IwlXT+3d5Dq9DfYOrhTkauc0LsYfYfGcMSx5exzD7ny9JKlfkZmaSEpiNP6tu1ot5uyMJNw8y8Ts6VfhICGnfMyOruSbY85MTWThWxP49v37SIjdD0BBXhYAO1Z/xNezb2fl/OnkZtXq1c6NTm5WEs4epe+gd3b3r1AXcjKTcfEoXa92Dq4U5GWQm5mEi3u535bsNwRr5v+NZR/ewfE9pT1/Xv6hxEdpB7VxR9aTk3mxjpbs6qSs2aehqmlL/BEpZQ+gJzBdCOENOAMHpZTdgW3Aq+ayLwDdpJRdgGnmYS+jvcGlFzAUeFcIcaVZGgHcBYQDdwkhAs0HBPOBiVLKrpQ+f/Zq05kGfCSljDDHmFjZQgghpgoh9gsh9q/6cUG1VkClR/ii8lfV7d66lvi444ya8EC15mENVYlTVvpKW8syh3//HKHTE9LV8nxdelIs+ze8R//xr9c21KvM2RxjNTei3yNNfLzKyLGzJnqFatU8JEBwKR0+XGlk3nojo3rosLP2VSGVBHrNFxiW4+EdwD/nrGTme+s5sOMXsjOtn1Qqb51WoU6Y601A66488OJa7n7uJ/b99gWG4sKSIkWFuaxdMJ3Bd7yEvTXPddawHgsEzm6+PP7W7zz88kqGTXyB1QufozA/B5PJQHb6JVq26c5DL62geXA3fl/+13Zn17tKq0L5Glt5na58m9R+e/uT3zL5Hz8z5tH5HNv1LRdO7wNg6J2zObZrKcs+vIOiwlx0etvaRF8jJpOs0aehqukubLoQ4nbz34FAKGACrhxyLQF+Nv8dCSwVQqwEVpqH3QKME0LMMH93AILMf2+WUmYCCCGOA60AT2C7lPIMgJQy7TrT2Q28LIRoCfwspYytbCHKvuR95/Hcav0veXr7knb5Usn39NRkPLyaVSh3/MifrP3pK2a++SW2ttZpqV7P8T1Lidn3EwA+LcPIzSyNMzfrEk6ulnE6u/mRV+boOzczqaSrHCD24EoSTm7l1kcWIsps4LmZl9i89GkGTXobN+8gaqNnqKBbiJZsL6RK3JwFXNb+S9ycBDn5luWz87ThV7g5CbLLlQE4Fi+ZMljHtmPQNVjwR7TW+k7PgYxcrWV+odZv9C3l7uVPRlrp+s5Mu1Sj1rSbpy9+LUI4c/JAyYVv1uLi4U92RmmM2RlJOLv7ViyTfhFXD39MRgOFBdk4OHlYlPHyD8HWzpHUizH4BYVjNBazZsF0OvS8jbZdb7FqzK6e/mSll4k5PQmXcjG7mmN28zTHnJ+Ng7MHQoiS0xT+rcLw8AkiLfkM/kFh2No50i5iBAAduo8ictdPVo27oXN29yM3o7Q1nJt5CWe3cnXB3Y+cjIu4mOtCUUE29k4euHj4WbSky/7W2dyz5+TiTXDYzSSfi6R5m154+rbhtqlagykj5QznTljnOprquNEubKt2S1wIMQS4GbjJ3Co+hJY8y7uypsYA/wf0AA6YX4Yu0FrVEeZPkJQy2ly+sMw0jGgHGoKrHDNWNh0p5bfAOCAf2CCEGFbd5bye4NDOJF1MICXpPIbiYvbu3EBEr8EWZc6ePsHiz97i6Zc+xM3jrzvX1qnvvUx4egUTnl5Bq47DOXXoF6SUJJ87jJ29q0WCBnBy88XW3pnkc4eRUnLq0C8EddRWWWLMDo5u/5Kb7/8UG7vS/urC/Cw2Lp5Gz1uexa9V91rHvD9WMn+9kfnrjZw8L+nSWkvQLbyhoBhyCizL5xRAUbE2HqBLa0FMolZFvMo0ANu1EKRmacMz8yDYT6vyzg7g7SpIz6l16BZatgkj9dJZ0pITMRiKOLLnVzp2H1ql32akXqK4SFvQvNxMzsYeollAsHUDBPyDwslIiSczNQGjoYiYg2sJCbPcRELChhG9dwUAsUc2EBjaFyEEmakJmIzaRQdZaedJTz6Dm1cLpJT89t3LePm1ofvQhyvMs7YCWoWTnhxPxmUt5uj9a2nbxTLm0C7DOLZHi/nEwQ0EtddizstOw2TSLozMSEkgPTkeD59AhBCEhA/lXMyfAJw9uRufgBCrx96Q+QaGk3H5LFlpiRgNRZw6vI7WnSzXa+tOwzh5QGt/xR3dQIu22npt3WkYpw6vw2goIistkYzLZ/EN6kJxUR5FBdqGVVyUR0LMH3j5twMgL0e7iEWaTBz47XM69a2buy+uRZpq9mmoRHWPSsznnR+VUt4mhOgAHAZGAb8Dd0spvxdC/BvwA54BgqSU8UIIW7Ru7fbATMANeFpKKYUQ3aSUh4QQDwE9pZRPmee1BpgLRAEHgUFSyjNCCC8pZZoQYvZVptMGOGMe9iEQL6X88FrLVd2WOEDkgZ18/9VcTCYTA4aPY+zkR1n57We0btuJiN6DmfvqNM6fPYW7pw8AXs38mf6SFsbbLz3CxfPxFBbk4+LqzkNPvkJYt35Vnvcfxx2vXwjtqHP36jc4H7tTu8Xsjtn4tAwDYOUntzPhaW2ndznxGNuXv4jRUEjL0IH0ve3fCCFY9t5ITMYi7B21VlizwK70n/Aah3//jMht83HzblUyr5EPf4mji3elcRQVV28rGNVDu9rcYIRVfxq5aG4t/32UnvnrtR1ygBeM66PdYhZ3UbL+gDaPSQN0eLsKJJCZK1m3z0R2Prg4wrg+OlwdtQOEXdEmjsZf/b89vG11OsJLnTi8jdVL3sZkMtFr8O0MGz+NjT99QsvgznTqMYyEuKMs/nA6+XlZ2Nra4eLuw3PvrCbm6C7WfvtfhBBIKek34h76DLuzWvO+mKqvUrkzUdvYtmI20mSkc9+J9L7lcXav+wjfwDBCwodjKC5kw5J/kZwYjYOTu3aLmU8g0ftWsu+3+ej0Ngiho8/IJ2nb5WbOx+1n2cf34hPQDnTagVL/Mc8S3HnwNeOwr0bnVNyxbWxepsUc3m8i/W59nB2rP8I/KIzQrlrMa77+F0kJ0Tg6uTPubx/g0SyQkwc3sGPNx+h0enQ6PQPGPl1yAJCZep41X8+kMD8LJxcvRj8wBzev5teMw29k+6oHXUUR37yH9+De2Pl4UpiUSuysT0hYaL1egdjlJ6467mz0Nv5YNRtpMtGh90R6DJ/G3g0f06xlGMGdh2EoLmTz9zO5fF6rCyPufR8370AADmz+nBN7lyP0evqPe4lWHQaRlZrA+kVPAdrV76HdxtJjuHYmNXLHYo7tWgpAm/Bb6HPrsxa9e2X9Y9xVRtTSjM/yatQUn/u4U53EU1s1SeL2aN3iLYCTQDPgNWAN8AEwGshEO6+dgZbc3dFazUuklG8LIRyBD4F+5uHxUsqxV0viUsqtQohbgdlovQfJUsoR15jOi8B9QDFwCbinTBd8pWqSxOtTVZN4Q1HdJN4Q1DSJ16eqJvGGojpJvKGoiyRe166VxBuqukriz31as339e084N8gdQrXPiUspC4FbKxl1pRPzP+WGD6hkGvnAY5UM/xr4usz3sWX+/hX4tYrTmQPMucoiKIqiKE1UQ75IrSbUE9sURVGUJuMGu65NJXFFURSl6WjID26pCZXEFUVRlCbDdIM1xVUSVxRFUZoM1RJXFEVRlEZKJXFFURRFaaRusByu3mKmKIqiKI2VaokriqIoTYbqTlcURVGURupGewGKSuKKoihKk6Ge2KYoiqIojZRqid+gFq0suH6hBqR5y8b15oiwdo3rxRwAc2ftqO8Qqu2uaYPqO4RqOR6ZXd8hVFtII3yZSOjEDvUdQvUVn6yTyapz4oqiKIrSSKkkriiKoiiN1I322FV1n7iiKIrSZEiTrNGnNoQQXkKITUKIWPO/npWUiRBC7BZCRAkhIoUQd1Vl2iqJK4qiKE2GlLJGn1p6AdgspQwFNpu/l5cHPCCl7AyMAj4UQnhcb8KqO11RFEVpMurpFrPxwBDz34uArcDzZQtIKWPK/H1BCJEMNAMyrjVhlcQVRVGUJqOeLmzzk1JeBJBSXhRC+F6rsBCiN2AHxF1vwiqJK4qiKE1GTbvGhRBTgallBs2TUs4rM/43wL+Sn75czfkEAN8AD0opTdcrr5K4oiiK0mRI03XzYuW/0xL2vGuMv/lq44QQSUKIAHMrPABIvko5N2At8G8p5Z6qxKUubFMURVGaDJNJ1uhTS6uAB81/Pwj8Ur6AEMIOWAEsllIuq+qEVRJXFEVRmox6ujr9bWCEECIWGGH+jhCipxDiS3OZO4FBwENCiMPmT8T1Jqy60xVFUZQmoz4ubJNSpgLDKxm+H3jU/PcSYEl1p61a4oqiKIrSSKmWeC1NGeFEeIgdRQbJwtU5nEsyVigzYbAjN4Xb4+Sg4+m5aSXD+4XbM2m4ExnZ2oUWW/YXsPNIodVjvLWXjtAWOoqNsPIPAxfTKpYJ8ILb+9tgo4fY8yZ+3afFNKSrjh6hOnLN74fZfMhI7HmJTsD4fnoCvAQ6AUdOm9hxrGYXjFxLTOQO1i2djclkosfgSQwe+3eL8WdO7GPdt3NISojhzifeI6zXyJJxi+b+nYS4I7QK7c79z35u9diu5ZmpIdzUw5uCQiOzPzpJTFxOhTLvvRaOt5cder3gSFQm738eS9lrbu6+vSVPPhLCmHv/IDPLYNX4zkbvYMfKt5AmE536TqLH8KkW442GIjZ9+zwpCVE4OHsw8oH3cfNqSX5uOuu/fobkhGN06DWBwRNfKflNzME17P/tC4QQOLv5MuLed3F0qfBgKquZONiezsG2FBVLlmzMJzGlYv0b28+e3h1tcbIXzPi09GUrQ7vZcVOYLSYT5ORLlm7KJz279i20cyd2sHOVtl479p5E92EV1+vm758nJTEKBycPRtynrVeAg1u+IHrvcoROx4DxLxPUfiAAS2YPw9beGSH06PR6Jj2zHIDLF06wffmrFBfl4erZgpvvmYudg0utl6Equsyfje/oIRQlp7K9221/yTyt5UZ7drpqiddCWIgtvl56Xv48g2/W5XLvKOdKy0XGFjN7YWal4/YdL2LWV5nM+iqzThJ4aAuBt5vg45UGVu82MrZP5W8TG9tXz6rdRj5eacDbTdC2uSgZt/u4ic/XGPh8jYHY89oG0Lm1QK+DT1cb+GKtgR7tdHhUvvg1ZjIZWb34DR54bh7T56zm6J61JJ8/ZVHGw7s5Ex+dQ5e+Yyr8fsCtjzBp6jvWDaoK+vbwIrC5E1Me28u7/xfDjMdDKy33n3eO89D0A9z/5H483G0Z2r9ZyThfH3t6RnhyKdn6b9czmYxs+3kWt02dzz3PryHm4FrSLlmu1+N//oS9oxv3v7yRroMfZNea9wCwsbGnz63P0H/cTMtpGg3sWDmb259YzN3/WoV38/ZE7qx2z2CVdWptg6+nnllf5/D95gLuGu5Yabljpw3M/S63wvDEFCPvfpfL20tzOXyqmAkDHWodk8lkZMeKWYz923ymzFjDqcNrSUuyXK/Re7X1eu8LG+ky6EH2rNPWa1rSKU4dXseUGWsY++iX7Ph5FiZTaYNg3LTF3PnsypIEDrB12b/pO/o57npuNcFhIzi89ataL0NVJS76mb1jH/3L5mdNJmmq0aehuqGSuBDiL+1ZiGhnx56jWuI9fcGAk4MOd2dRodzpCwYyc+vn6K9DoOBwnFYBEy9LHOwELuX2dy6OYG8rSLysxXg4zkTHoIrLUZaUYGcDOgE2NmA0QWGxdWNPPB2Jt18QXr6B2NjYEd5nNNEHt1iU8WzWAv+g9ghdxaoc0vkm7BysfGRRBQP7erN+yyUAok5m4+Jsg7dnxVfH5uVrO2m9XmBro6PstTNPPxrCZwtPUxfvakg6F4m7TxDu3oHobewI7Taa08c2W5Q5fWwzHXpNAKBtl5Ekxu5GSomtvRPN2/RAb2O5PBLt4p/iojyklBQV5ODsfs3nWdRKeIgNe6OLAIi/ZMTRDtycKtbZ+EtGsvIqrsTYRCPF5s6N+ItGPFyuXd+rItm8Xt3M67VtxGjioyzXa3zUZtr30NZrSPhIzkJZ00kAABp5SURBVJvXa3zUZtpGjEZvY4ebV0vcfYJIPhd5zfllpJwhoE0vAALb9eP00Y21XoaqStu5n+K0/2/vzuOrKu88jn++CWHfQUBEKmAQERABEdcqWlyx4t5R2yLW0dqK05lpx47WrWqt2gp2WlurlLFYq+NOVbTUuqEoKIsLLoi4oCA7CUu23/zxnEtuQlZIPOckv/frlZe5NzfJN4fjfc55lt9T9Y1J0sVRO70xxd6dLqkdcD/QB8gFrgM+BKYA7YBthAkBxcDvgFFACfAjM3tW0neBE4HW0evHSvpPwky/VsDDZnZVY2Tv0j6HtRvLr9DWbSqjc4ccNhTu2KVenRGDWjKwbwtWri3lr89sZt2mhr3i69BWFd7ENm42OrYVBVvKn+u4w2vC92WMHpTD/gNyWLHGmDWvlK1F8PZyY9Ce8B9ntCAvF56aV8qWogaNzsZ1q+jUtbx2QseuPfl0ac1vbEnQvVsrVq0u71VZtWYb3bu1ZM26HQ/QrdcMZfDADrwyfy3/nPMlAIeO7sbqNdv44KMd7yAbQuGGlXTovPv2x+0792Ll8oWVXrNq+2tyclvQsnUHthaur7Z7PDc3jyNPv4q/3HwyeS3b0nm3r1Xoam9ondupQvf3+gKjU3tV2WDX5uD9WvL2R7s+XFG4cSXtso5ru069WPVxxeNasGEV7Ssf183rKdywkp59h1f43sKNK6NHYuadkwDYb8xZDB4T9sXo2iufj976B/2GHM3ShU9RsOHzXf4bmoMkN8g7Iwl34scBK8xsfzMbAjwF/BWYbGb7A8cAW4BLAMxsKPAtYLqkTB/YwYTqNmMljQPygdHAcGCkpCOq+sWSLpQ0T9K8Ja9Or3/yKi7e63N6LPygiMv/Zx3X/HED7ywr5vzxDT+eVdX9RZ2WS0Qvee3dMqY8XMIdj5dQsNk4dlTojt+juzCDWx4o4baHSzhkcC5dGjp+FTmlXb9jamxVJqzmkP/7VYv55rdfJi8vhxHDutCqVQ7fObMvf5zxUeMFrCpL5eNa1TlSw6EvLS3mzTn3cfa/P8zEq5+n2+4DmT+72roYu6yhToNRg/LYs2cOs+c3wBVoXY5rFS8SVR/uzAGfcMm9nHHZQ5x4wZ28OedeVnz4GgBHnXkDb86ZwQO3nUrRtkJycvN2JX2zEdMSs0YT+504sBi4RdJNwExCsffPzew1ADPbCCDpMOD26LklkpYDA6Of8YyZZaZrjYs+3ogetyc06s9X/sXZFXi+d8OaOv0rHTmyFUcMD9cOy1aU0LVj+XVQlw45bKjHnXRh1t3w8wu2cepRbev8vTUZvU8OI/JDrhVrjI5ZP7ZjW7FpS8XXZ+7Oy18Dm6JshVlDsvPfL+NfxoZTZlg/8f6KMsosvObjL43e3cS6goY72Tt27cmGtV+U51y7kg6dG6+LdlecekJvxh8b7rDeeX8TPbq32v61Ht1asXpt9Y1EUbHx4tw1HH5QN9auK2L3nq3509RRAOzWvRV33zaS7/3oddaub5jxinade7JpffldW8H6L2jXsUeVr2nfuRdlpSUUbd1E67bVb6i0+rMlAHTq3heAvYcfz+uz72yQvBmHD8vjkKGhG//jL0rp0qH8nO3cXmyo57m3z565HDu6JVMe2ExJ3TvPqtWuU08Ks45r4YYdj2v7Tj0pqHRcW7XtTPvOPSvcSWd/b7tOPQFo274b/YYcw6qPF9G7/4F06dGf8RfeDYSu9Y+XPLfrf0QzULaTFduSKvY78WjnlpGExvxGYALVXNPW8GOy+x0F3Ghmw6OPvc2swWZ8/HP+tu0T0Ra8V8SYoeHNun/vFmzZZvUa+84ePx+e35Iv1jTAOwnw6rvlE9He+biM4QPCP3Of7mJrsVFQqREv2BIakj7dQ57hA3JY8kn4O7LHz/ftm8Oq9eH5DYXQv1f4uXktws9evaFhr1b36DeUNSuXs/bLTykpKWLx3CcYdMBRDfo7GspDT6xg4uT5TJw8nxdeWc1xY8MwwH77dKBgc8kOXeltWudsHyfPzYGDR3Vl+aeb+XB5IePPe5kzLpjLGRfM5cvV2zj/svkN1oAD9NxzKBu+XM7GNZ9SWlLE+288Qb8hYyu8pt9+Y1ny2iMAfLBoFn32HlNjL0i7Tj1Y+8VSthSEa+lP3ptDl579GywzwAuLirlpRiE3zShk0dISRu8bjt9evXLZWkS9utL77JbDWUe34Q+PbakwtLQreuw5lPWrl7NxbTiuHyx4gr0GVzyuew0ey7vzw3FdungWe0THda/BY/lgwROUlhSxce2nrF+9nB59h1FctJmirWFlQ3HRZj557yW69gr3LpsL1gChjOj8v9/B4DFnN8jf0dT5mHgDk9QbWGtmf5ZUQCgw31vSgWb2mqQOhO7054FzgH9IGgj0Bd4FRlT6kbOA6yTNMLMCSXsAxWZWZa3aXbF4aTFD927J9Rd3pqjY+NPM8mVEP5vUiWvvChM/TjuqLQft15KWefDLH3TmhYXbePyFLYw9sA3D8/MoLYPCrca0mTsuQ9pV739mDNzDmDyhBcUl8Mic8guFi05qwR0zw1jgzLllnHJILnktwhKzzCz0cSNy6dVVGGHc8fFXwve/+m54/SUnh1NowdIyVta4YV795ea24KTzrmD6zReEJWZHnErPPvn8/aGp7LHXEPYdMZZPP1zMvVN/yJbCjSx541n+8dDtXHrjTADuvP5cvvz8Q4q2buaXlx3JhEk/J3/oYQ0bsgovz1vLwaO68tc/jN6+xCxj2pSRTJw8n9atc/nFlfuR1yKH3Fwxf+F6Hn1yRaNngzAWe8SpV/LoHyaFJWajT6Nbr3zmPjmVHnsOod+QsQw+6HSeuffH3HP9OFq17cSx3/7V9u+fft1YirYWUlZazIdvzuab/3oXXXvtzehjL+Gh35xLTm4LOnTpzdHfurHR/oa3PiphcL8W/Oy77SkuCUvMMn5yTjtumhGu6795WCtG7pNHXh5cO6k9L79VzJOvbOOUw1vTKg/OPzFcpa7bWMYfHt9S5e+qq5zcFhx+ypXMvDMc10GjT6Nrr3xenTWV3foMod9+Yxk0+nRm3/djZvxiHK3bduIb54Tj2rVXPgP2P577bj4R5eZy+ISfkZOTS8GmNTw1/QdAmP2ef8BJ9B0Ulp598MbfeHPODAD6Dx3HoANP3aX89TH8nlvp9vXRtOzehbHLnuP9a2/nk2n/95X9/l1Rhz1FUkVx9/VLOha4GSgjTF67mHA3fTvQhtCAH0OYzHYH4a698sS2UWb2g6yfOZmoCg5QAJxrZjVu6VbX7vSk6N2nY9wR6mXIwKqXtiXZlOtfiDtCvZ11UZXTPxLrvfc31f6ihBnQv0PcEeot/7RBcUeotxOL322UCTAnnL94p97rn7h7aCIn5MR+J25mswh3z5WNqeK571bx/X8C/lTpuSmE2e3OOefcdknuGt8ZsTfizjnn3FclyYVbdoY34s4555oNvxN3zjnnUsqa2BIzb8Sdc841G34n7pxzzqVUU1ti5o24c865ZqPM78Sdc865dGpqY+Kxl111zjnn3M7xO3HnnHPNhk9sc84551LKJ7Y555xzKdXU7sRj3wClqZN0YbRveWqkLXPa8oJn/iqkLS94Zld/PrGt8V0Yd4CdkLbMacsLnvmrkLa84JldPXkj7pxzzqWUN+LOOedcSnkj3vjSOFaUtsxpywue+auQtrzgmV09+cQ255xzLqX8Ttw555xLKW/EnXPOuZTyRtw555xLKW/EnXPOuZTyRrwRSWoXd4a6kDRQ0mxJb0aPh0m6Iu5cNZHUVtKVku6MHudLOinuXNWRNFlSRwV3SXpd0ri4c9UkpefFGXV5LikkDZDUKvr8SEmXSuocd67aSDpM0sTo890k9Ys7U3PljXgjkHSIpLeBd6LH+0v6bcyxanIncDlQDGBmi4CzY01Uu2nANuDg6PGnwM/ji1Or881sIzAO2A2YCPwi3ki1SuN5cXkdn0uKB4FSSXsDdwH9gHvjjVQzSVcBP6H8uOYBf44vUfPmG6A0jl8DxwKPAZjZQklHxBupRm3N7FVJ2c+VxBWmjgaY2VmSvgVgZltU6Q9ImEy2E4Bp0TmR5LyQovNC0vGEY7uHpKlZX+pIQjNHysysRNIE4DYzu13SG3GHqsUE4ADgdQAzWyGpQ7yRmi9vxBuJmX1S6c2vNK4sdbBa0gDAACSdDnweb6RaFUlqQ3nmAYQ786SaL+lpwp3W5dGbXtL3REzTebECmAecDMzPen4T8G+xJKqb4uhC9DvA+Oi5vBjz1EWRmZmkzHmRimHDpsob8cbxiaRDAJPUEriUqGs9oS4hVF0aJOkzYBlwbryRanUV8BSwp6QZwKHAd2NNVLNJwHDgQzPbLKkboUs9yVJzXpjZQmChpBlmluQ778omAhcB15vZsmhsOeld0/dL+j3QWdL3gPMJQy8uBl6xrRFI6g5MAY4hdKM+DUw2szWxBqtFdEWdY2ab4s5SF1FDOIZwjF8xs9UxR6pW1HV+DtDfzK6V1BfoZWavxhytVmk6LyQtI+o5yGZm/WOIUydRj1JfM3s37ix1JekbhPkdAmaZ2TMxR2q2vBF3RLNhvw3sRVbvjJldGlemupA0jB0zPxRboBpI+h2h+3ysme0rqQvwtJkdGHO0aqXxvIgu7DJaA2cAXc3sZzFFqpGk8cAtQEsz6ydpOHCtmZ0cc7QqScolNNrHxJ3FBd6d3ggqTazJ2ADMM7NHv+o8dfAE8AqwmOSP0wIg6W5gGPAW5ZkNSGQjDhxkZiMyk5bMbF001JJkqTsvqujtuk3Si0AiG3HgamA08E8AM1uQ5OVaZlYqabOkTma2Ie48zhvxxtIaGAQ8ED0+jdDYTJJ0lJldFluyqrU2sx/FHaKexpjZ4LhD1ENxdBeTmQy0G8lvGFN3XkgakfUwBxgFJHnmdImZbag0CTbp3aNbgcWSngEKM08muYemKfNGvHHsTeg2LYHtXalPA98g3NUkzT3RBJWZZM3wNrO18UWq1cuSBpvZ23EHqaOpwMNAD0nXA6cDiS6cQjrPi1uzPi8BPgLOjCdKnbwp6V+AXEn5hEmwc2LOVJu/RR8uAXxMvBFIehcYneluktQJmGtmgyS9YWYHxJuwIkmXANcD6ym/C7CETwY6Angc+ILQwIiQeViswWogaRBwNCHrbDNL8oqFVJ4XaSOpLfDfhEliALOAn5vZ1vhS1S4aChoYPXzXzIrjzNOceSPeCCRNItxl/ZPwhn0EcAPwF+BqM/vP+NLtSNJSwphtYmd3VybpA+BHVBqvNbPlsYWqhqQcYJGZDYk7S32k9LzoRFh+mCmu9BxhopiP3zYQSUcC0wm9HAL2BL5jZs/HGKvZ8rKrjcDM7iKsW15C6EK9AnjPzAqT1oBH3gI2xx2inj42s8fMbJmZLc98xB2qKmZWRljD3DfuLPWUxvPibkKBlzOjj42EEr2JJOmZ7FrpkrpImhVnpjq4FRhnZl83syMI1Sl/HXOmZsvHxBuBpAuAyUAfYAFhLfPLwNg4c9WgFFgg6Vkqjn0meaLKEkn3ErrUszMndXb67sBbkl6l4mSgRC4liqTxvBhgZqdlPb5G0oLY0tSuu5mtzzyIVi30iDNQHeRlr2k3s/ckJb3KXJPljXjjmAwcSChAclQ0FnpNzJlq8kj0kSZtCA1L9k5gSV5iluR//+qk8bzYIukwM3sRQNKhwJaYM9WkTFJfM/sYQNLXSP7s9HmS7gLuiR6fQ8VSt+4r5GPijUDSa2Z2YHQHcJCZbZO0wMyGx53NuaYsKpYyHehEGK9dSxivXRRrsGpIOo5Q2va56KkjgAvNLLFd6gpbp14CHEY4xs8DvzWzJO9d0GR5I94IJD1MqIl8GaELfR2hC+qEWINVIul+MztT0mKqLlWZuJnekn5sZr+UdDtVZ05kV6+kTZTnbUnY5KLQzDrGl6pqaTwvKpPUESDa/jXRojLNmfLBLyd9ImFUhnermZVGj3OBVmaWtvkTTYJ3pzcCM5sQfXp1NJ7YibBZR9JMjv57Uqwp6iezLGterCnqycwqFByRdAqhUlcSpfG8AHacnS4pDbPTWxF6DFoAgyWR8Jneswn7QhREj9sQ6mAcEluiZswb8UZmZs/V/qp4mFlmW8nvm9lPsr8m6SbgJzt+V7zM7PHo081m9kD21ySdEUOknWJmj0j6r7hzVCWN50WWu4E3KS/wch5hdvqpsSWqQXQ8z2LH8sFJbsRbm1mmAcfMCqL17i4G3p3ukPS6mY2o9NyiJHebVpN5h+eSQlJ2I5IpB/p1Mzs4pki1Sul5scPckyTPR4kKQw1L03iypJeAH5rZ69HjUcDtST6XmzK/E2/GJF0MfB/oLyl74k8H4KV4UtVM0vHACcAelTaa6Ugos5lU47M+z5QD/WY8UWpWy3mR9JKgaZud/iFhfkRqGnHCcMsDklYQeg16E3oTXAy8EW/e7gWeBG4Esrt2NyW4PvYKwnj4yVRc1rIJ+LdYEtWBmU2MO0M9pPG8yLgI+N9obBzCpNLvxJinNpsJa/Fnk561+P2AA4C+wATCpDzv0o2Jd6c3Y5K61vT1JL9hR/sw/y2qhpZY1c2iz0j4mzWSDgPyzWxaNIu6g5ktiztXdSRldl1rH/23gLAN8HwzS1zRF0lVXmCY2fSvOktdZYZUonPjBkIFt5+a2UExR2uWvBFvxiQto7yBUaUvJ3qjC0l/Bg4GHgSmJXUzkerepDMS/mZ9FWHsfh8zGyipN/CAmR0ac7RqRVX8RgGPEc7pE4HXiLYGNrNfxhivSpLaAH2zq6AlWWYTJ0k3AovN7N4kbuzUXHgj7lIrWgv8LcKafCPMQv6LmW2KNVgTERUrOgB4PfMGnYKJbbOA0zKzpyW1B/6P0O073xK2B33Uo3QL0NLM+kXFaq5NcjleSTOBzwjLzEYS5hy8amb7xxqsmfINUBwKzpV0ZfS4r6SkrmHeLirk8SBwH6E2+QTgdUk/jDVYFkm3Rf99XNJjlT/izleLIgtX+Qbbi3wkXV+gKOtxMfA1M9tCMiePXU2oF7AeIOry7xdnoDo4k7Bl6nFR3feuQBI3dmoWfGKbA/gtYY3qWOA6wiSxBwn13xMpuoM5HxhAqOE82sxWRetV3wFujzNflkx96VtiTbFz7pf0e6CzpO8RjvedMWeqzb3AK5IejR6PB/4SXYC8HV+sapWY2QapwmhWortHo8psD2U9/hz4vPrvcI3Ju9Pd9vXA2eNakhYmuXtM0v8Cf6yqspWko81sdgyxmhxJ3yBsMiNglpk9E3OkWkkaSXld7xfNLLHV/aKNRGYTVgGcBlxKKNF8UazBXGp4I+6QNJdQMvG1qDHfDXjaJ6o0HEn5hCVbg4HWmeeTPHkQtu+qlW9mf496OXJ9zkHDiY7pf5N1oQRcZ2ZbYw3mUsMbcYekcwjFGkYQdoA6HbiiclnTJKi0kcgOkrihCICkFwk1vX9N6OKdSPj/76pYg9Ug6kK/EOhqZgOiC5E7zOzomKM1SdFGIu3SsGmLSw5vxB0ACnueH024G5id1CVbGZKuBb4gjDmLsKdxhyQuIQKQNN/MRkpabGZDo+deMLPD485WnWh2+mhgbtYwy/b8btdFS+IuAkoJxYs6Ab8ys5tjDeZSw2enOyRNIdxt/Y+Z/SbpDXjkWDP7rZltMrONZvY7wphiUm2VlAO8L+kHkiYAPeIOVYttZrZ9prekFiR80lUKDY7uvE8BniDMrj8v3kguTbwRdwCvA1dI+kDSzdGGBklXKukcSbmScqIhgdK4Q1UmKTM7/VGgLWHi0kjCG3WSy4ECPCfpp0CbaILbA8DjtXyPq588SXmERvxRMyvGL5RcPXh3utsuKsN6GnA2oYJUfsyRqiVpL2AKcCjhTe8l4DIz+yi+VDuS9DZwPKGC2JFUqoyX8NK2OcAkKk66+qP5m0aDkXQpYWvXhYTqcn2BPyd5mMUlizfibruowMtZhLuCt81sfC3f4moRvUlfDPQnVLkS4aJDJLi0bTTJarqZnRt3luZGUgszS/KOfC5BvBF3SLoJOBVYCtwPPBRVYkosSdOootvRzM6PIU6tJP3OzC6OO0d9RCVMx2ePi7uGJakbYdXCYYTz+UVC2dU1sQZzqeEV2xzAMuBgM1sdd5B6mJn1eWtCydUVMWWpVdoa8MhHwEtRedjCzJNm9qvYEjU99wHPUz4p8xzgr4S65M7Vyu/EHQCSugD5VCxEskM1tKSKxm//bmZj486SdpLuMbPzJK0nrGuvwMyuiSFWk5RZeljpuXlmlobJpS4B/E7cIekCYDLQB1gAjAFeJtRST4t8wqQgt+tGRpXaPiY5NeibqmclnU0YxoJQaOlvMeZxKeN34g5JiwmbnbxiZsOjwi/XmNlZMUerVhWV274ALjezB2OK1GRkTcbrR8UhikRPxkuTrPNXQDvKl0fmAgVJrTzoksfvxB3AVjPbKglJrcxsiaR94g5VEzPrEHeGpsrMpgJT0zgZLy2yz99oaWeFoSzn6sobcQfwqaTOwCPAM5LWkeBJYgCSZleu4V3Vc27neQPe+KoZyppDKIHsXK28O91VIOnrhPrNTyVxaZGk1oTKZ89SsXhKR+BJM9s3pmjO1Vsah7JcsvideDMXzepeZGZDAMzsuZgj1eZfgcuA3oQNIzLFUzYBv4kxl3M7I3VDWS5ZvHZ6M2dmZcBCSamY2W1mU8ysH3A9MDz6fBrwIWFGvXNpUnko61ESPpTlksW70x2S/kHo0nuVikU9To4tVC0kLTKzYZIOA24AbgV+amYHxRzNuZ2S9KEsl0zene4A2gMnZT0WcFNMWeoqsyTnROAOM3tU0tUx5nFul6RgKMslkDfiDqBF5TcQSW3iClNHn0n6PaE85U2SWuHDQ865Zsa705sxSRcD3yfssLU060sdgJeSvIOVpLbAccBiM3tf0u7AUDN7OuZozjn3lfFGvBmT1AnoAtwI/FfWlzYleZ9r55xzgTfizjnnXEr5GKJzzjmXUt6IO+eccynljbhzzjmXUt6IO+eccynljbhzzjmXUv8PCrgjsAxv4o8AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 576x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "correlation = students[['age', 'traveltime', 'studytime',\n",
    "                        'failures', 'freetime', 'goout', 'absences', 'score']].corr()\n",
    "plt.figure(figsize=(8, 5))\n",
    "sns.heatmap(correlation, annot=True, cmap='coolwarm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "higher_education\n",
       "no     40.0\n",
       "yes    55.0\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='higher_education')['score'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "mother_education\n",
       "0.0    75.0\n",
       "1.0    50.0\n",
       "2.0    55.0\n",
       "3.0    50.0\n",
       "4.0    60.0\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='mother_education')['score'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "father_education\n",
       "0.0    65.0\n",
       "1.0    50.0\n",
       "2.0    55.0\n",
       "3.0    50.0\n",
       "4.0    60.0\n",
       "Name: score, dtype: float64"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students.groupby(by='father_education')['score'].median()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sex</th>\n",
       "      <th>age</th>\n",
       "      <th>address</th>\n",
       "      <th>mother_education</th>\n",
       "      <th>father_education</th>\n",
       "      <th>mother_job</th>\n",
       "      <th>studytime</th>\n",
       "      <th>failures</th>\n",
       "      <th>paid_additional_classes</th>\n",
       "      <th>higher_education</th>\n",
       "      <th>romantic</th>\n",
       "      <th>goout</th>\n",
       "      <th>score</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>F</td>\n",
       "      <td>18</td>\n",
       "      <td>U</td>\n",
       "      <td>4.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>4.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>F</td>\n",
       "      <td>17</td>\n",
       "      <td>U</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>3.0</td>\n",
       "      <td>30.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>at_home</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>2.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>F</td>\n",
       "      <td>15</td>\n",
       "      <td>U</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>health</td>\n",
       "      <td>3.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>2.0</td>\n",
       "      <td>75.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>F</td>\n",
       "      <td>16</td>\n",
       "      <td>U</td>\n",
       "      <td>3.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>other</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>2.0</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  sex  age address  mother_education  father_education mother_job  studytime  \\\n",
       "0   F   18       U               4.0               4.0    at_home        2.0   \n",
       "1   F   17       U               1.0               1.0    at_home        2.0   \n",
       "2   F   15       U               1.0               1.0    at_home        2.0   \n",
       "3   F   15       U               4.0               2.0     health        3.0   \n",
       "4   F   16       U               3.0               3.0      other        2.0   \n",
       "\n",
       "   failures paid_additional_classes higher_education romantic  goout  score  \n",
       "0       0.0                      no              yes       no    4.0   30.0  \n",
       "1       0.0                      no              yes       no    3.0   30.0  \n",
       "2       3.0                      no              yes       no    2.0   50.0  \n",
       "3       0.0                     yes              yes      yes    2.0   75.0  \n",
       "4       0.0                     yes              yes       no    2.0   50.0  "
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "students_for_model = students.loc[:, ['sex', 'age', 'address', 'mother_education', 'father_education', 'mother_job',\n",
    "                                      'studytime', 'failures', 'paid_additional_classes', 'higher_education', 'romantic',  'goout', 'score']]\n",
    "students_for_model.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As a result of the exploratory data analysis the impact of student's social conditions on their math scores the following conclusions were obtained:\n",
    "\n",
    "1. There were a lot of missing values in the data, as well as several erroneous ones. Erroneous values were deleted and the missing ones were replaced.\n",
    "2. Outliers were detected in many columns, but their analysis did not reveal the need to delete them, so they were left in order to obtain more reliable data for the model.\n",
    "3. Statistical analysis allows us to conclude that from the nominative variables, the following parameters have the greatest impact on students' math scores: sex (slightly affects the math scores), address, mother_education, father_education (interestingly, the highest number of points are received by students whose parents do not have an education and slightly lower by those whose parents have a higher education), mother_job (slightly affects the math scores, more points are received by students whose mother works in the health sector), paid_additional_classes(interesting, that slightly affects the math scores), higher_education (higher score for students who are going to graduate), romantic (interesting, that significantly affects the math scores)\n",
    "4. Based on the correlation analysis of numerical variables, math scores are most affected by: 'age', 'studytime', 'failures','goout', 'score'. Interestingly, the most significant influence. Interestingly, the most significant influence is the number of failures (correlation coefficient -0.34) and almost does not affect the number of absences (correlation coefficient 0.0059). It is also interesting that studytime has a low impact on the score (correlation coefficient -0.11)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
