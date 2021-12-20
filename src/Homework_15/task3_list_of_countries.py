"""
This module forms auxiliary list
"""


city_name = '''Afghanistan
Albania
Algeria
Andorra
Angola
Antigua and Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Top of Page

B
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia and Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina Faso
Burma
Burundi
Top of Page

C
Cambodia
Cameroon
Canada
Cabo Verde
Central African Republic
Chad
Chile
China
Colombia
Comoros
Congo, Democratic Republic of the
Congo, Republic of the
Costa Rica
Cote d'Ivoire
Croatia
Cuba
Curacao
Cyprus
Czechia
Top of Page

D
Denmark
Djibouti
Dominica
Dominican Republic
Top of Page

E
East Timor (see Timor-Leste)
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Ethiopia
Top of Page

F
Fiji
Finland
France
Top of Page

G
Gabon
Gambia, The
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guinea-Bissau
Guyana
Top of Page

H
Haiti
Holy See
Honduras
Hong Kong
Hungary
Top of Page

I
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
Top of Page

J
Jamaica
Japan
Jordan
Top of Page

K
Kazakhstan
Kenya
Kiribati
Korea, North
Korea, South
Kosovo
Kuwait
Kyrgyzstan
Top of Page

L
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Top of Page

M
Macau
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Top of Page

N
Namibia
Nauru
Nepal
Netherlands
New Zealand
Nicaragua
Niger
Nigeria
North Korea
Norway
Top of Page

O
Oman
Top of Page

P
Pakistan
Palau
Palestinian Territories
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Poland
Portugal
Top of Page

Q
Qatar
Top of Page

R
Romania
Russia
Rwanda
Top of Page

S
Saint Kitts and Nevis
Saint Lucia
Saint Vincent and the Grenadines
Samoa
San Marino
Sao Tome and Principe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Saint Marten
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Korea
South Sudan
Spain
Sri Lanka
Sudan
Suriname
Swaziland
Sweden
Switzerland
Syria
Top of Page

T
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tonga
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Tuvalu
Top of Page

U
Uganda
Ukraine
United Arab Emirates
United Kingdom
Uruguay
USA
Uzbekistan
Top of Page

V
Vanuatu
Venezuela
Vietnam
Top of Page

Y
Yemen
Top of Page

Z
Zambia
Zimbabwe'''

list_of_country = city_name.split('\n')
result_list_of_countries = []

for city in list_of_country:
    if not any((len(city) == 1, city == '', city == 'Top of Page')):
        result_list_of_countries.append(city)
