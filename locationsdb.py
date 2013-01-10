us_states_items = [("AA","Armed Forces Americas"),("AE","Armed Forces Europe, Middle East, & Canada"),("AK","Alaska"),("AL","Alabama"),("AP","Armed Forces Pacific"),("AR","Arkansas"),("AS","American Samoa"),("AZ","Arizona"),("CA","California"),("CO","Colorado"),("CT","Connecticut"),("DC","District of Columbia"),("DE","Delaware"),("FL","Florida"),("FM","Federated States of Micronesia"),("GA","Georgia"),("GU","Guam"),("HI","Hawaii"),("IA","Iowa"),("ID","Idaho"),("IL","Illinois"),("IN","Indiana"),("KS","Kansas"),("KY","Kentucky"),("LA","Louisiana"),("MA","Massachusetts"),("MD","Maryland"),("ME","Maine"),("MH","Marshall Islands"),("MI","Michigan"),("MN","Minnesota"),("MO","Missouri"),("MP","Northern Mariana Islands"),("MS","Mississippi"),("MT","Montana"),("NC","North Carolina"),("ND","North Dakota"),("NE","Nebraska"),("NH","New Hampshire"),("NJ","New Jersey"),("NM","New Mexico"),("NV","Nevada"),("NY","New York"),("OH","Ohio"),("OK","Oklahoma"),("OR","Oregon"),("PA","Pennsylvania"),("PR","Puerto Rico"),("PW","Palau"),("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),("TN","Tennessee"),("TX","Texas"),("UT","Utah"),("VA","Virginia"),("VI","Virgin Islands"),("VT","Vermont"),("WA","Washington"),("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming")]
us_states_dict = dict(us_states_items)
state_selection_items = [('', ''), ('--', 'Not in USA')] + us_states_items

us_states50_items = [("AK","Alaska"),("AL","Alabama"),("AR","Arkansas"),("AZ","Arizona"),("CA","California"),("CO","Colorado"),("CT","Connecticut"),("DC","District of Columbia"),("DE","Delaware"),("FL","Florida"),("GA","Georgia"),("HI","Hawaii"),("IA","Iowa"),("ID","Idaho"),("IL","Illinois"),("IN","Indiana"),("KS","Kansas"),("KY","Kentucky"),("LA","Louisiana"),("MA","Massachusetts"),("MD","Maryland"),("ME","Maine"),("MI","Michigan"),("MN","Minnesota"),("MO","Missouri"),("MS","Mississippi"),("MT","Montana"),("NC","North Carolina"),("ND","North Dakota"),("NE","Nebraska"),("NH","New Hampshire"),("NJ","New Jersey"),("NM","New Mexico"),("NV","Nevada"),("NY","New York"),("OH","Ohio"),("OK","Oklahoma"),("OR","Oregon"),("PA","Pennsylvania"),("PR","Puerto Rico"),("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),("TN","Tennessee"),("TX","Texas"),("UT","Utah"),("VA","Virginia"),("VI","Virgin Islands"),("VT","Vermont"),("WA","Washington"),("WV","West Virginia"),("WI","Wisconsin"),("WY","Wyoming")]
us_states50_dict = dict(us_states_items)

canada_states = [("AB", "Alberta"),("BC", "British Columbia"),("MB", "Manitoba"),("NB", "New Brunswick"),("NL", "Newfoundland and Labrador"),("NS", "Nova Scotia"),("ON", "Ontario"),("PE", "Prince Edward Island"),("QC", "Quebec"),("SK", "Saskatchewan"),]

us_states50_and_canada_states = us_states50_items + canada_states


def country_iso_to_2digit(isonumber):
    for c in COUNTRIES_IN_DETAIL:
        if c[2] == str(isonumber):
            return c[0]
    raise LookupError, "Cannot lookup %s" % isonumber


def country_2digit_to_name(countrycode):
    for c in COUNTRIES_IN_DETAIL:
        if c[0] == str(countrycode):
            return c[3]
    raise LookupError, "Cannot lookup %s" % countrycode


def country_2digit_to_iso(countrycode):
    for c in COUNTRIES_IN_DETAIL:
        if c[0] == str(countrycode):
            return c[2]
    raise LookupError, "Cannot lookup %s" % countrycode


COUNTRIES_IN_DETAIL = (
('AF', 'AFG', '004', ('Afghanistan')), ('AX', 'ALA', '248', ('Aland Islands')),
('AL', 'ALB', '008', ('Albania')), ('DZ', 'DZA', '012', ('Algeria')),
('AS', 'ASM', '016', ('American Samoa')), ('AD', 'AND', '020', ('Andorra')),
('AO', 'AGO', '024', ('Angola')), ('AI', 'AIA', '660', ('Anguilla')),
('AQ', 'ATA', '010', ('Antarctica')),
('AG', 'ATG', '028', ('Antigua and Barbuda')),
('AR', 'ARG', '032', ('Argentina')), ('AM', 'ARM', '051', ('Armenia')),
('AW', 'ABW', '533', ('Aruba')), ('AU', 'AUS', '036', ('Australia')),
('AT', 'AUT', '040', ('Austria')), ('AZ', 'AZE', '031', ('Azerbaijan')),
('BS', 'BHS', '044', ('the Bahamas')), ('BH', 'BHR', '048', ('Bahrain')),
('BD', 'BGD', '050', ('Bangladesh')), ('BB', 'BRB', '052', ('Barbados')),
('BE', 'BEL', '056', ('Belgium')), ('BZ', 'BLZ', '084', ('Belize')),
('BJ', 'BEN', '204', ('Benin')), ('BM', 'BMU', '060', ('Bermuda')),
('BT', 'BTN', '064', ('Bhutan')), ('BO', 'BOL', '068', ('Bolivia')),
('BA', 'BIH', '070', ('Bosnia and Herzegovina')),
('BW', 'BWA', '072', ('Botswana')), ('BV', 'BVT', '074', ('Bouvet Island')),
('BR', 'BRA', '076', ('Brazil')),
('IO', 'IOT', '086', ('British Indian Ocean Territory')),
('BN', 'BRN', '096', ('Brunei Darussalam')), ('BG', 'BGR', '100', ('Bulgaria')),
('BF', 'BFA', '854', ('Burkina Faso')), ('BI', 'BDI', '108', ('Burundi')),
('KH', 'KHM', '116', ('Cambodia')), ('CM', 'CMR', '120', ('Cameroon')),
('CA', 'CAN', '124', ('Canada')), ('CV', 'CPV', '132', ('Cape Verde')),
('KY', 'CYM', '136', ('Cayman Islands')),
('CF', 'CAF', '140', ('Central African Republic')),
('TD', 'TCD', '148', ('Chad')), ('CL', 'CHL', '152', ('Chile')),
('CN', 'CHN', '156', ('China')), ('CX', 'CXR', '162', ('Christmas Island')),
('CC', 'CCK', '166', ('Cocos (Keeling) Islands')),
('CO', 'COL', '170', ('Colombia')), ('KM', 'COM', '174', ('Comoros')),
('CD', 'COD', '180', ('Democratic Republic of the Congo')),
('CK', 'COK', '184', ('Cook Islands')), ('CR', 'CRI', '188', ('Costa Rica')),
('CI', 'CIV', '384', ('Cote d\'Ivoire')), ('HR', 'HRV', '191', ('Croatia')),
('CY', 'CYP', '196', ('Cyprus')), ('CZ', 'CZE', '203', ('Czech Republic')),
('DK', 'DNK', '208', ('Denmark')), ('DJ', 'DJI', '262', ('Djibouti')),
('DM', 'DMA', '212', ('Dominica')),
('DO', 'DOM', '214', ('Dominican Republic')), ('EC', 'ECU', '218', ('Ecuador')),
('EG', 'EGY', '818', ('Egypt')), ('SV', 'SLV', '222', ('El Salvador')),
('GQ', 'GNQ', '226', ('Equatorial Guinea')), ('ER', 'ERI', '232', ('Eritrea')),
('EE', 'EST', '233', ('Estonia')), ('ET', 'ETH', '231', ('Ethiopia')),
('FK', 'FLK', '238', ('Falkland Islands (Malvinas)')),
('FO', 'FRO', '234', ('Faroe Islands')), ('FJ', 'FJI', '242', ('Fiji')),
('FI', 'FIN', '246', ('Finland')), ('FR', 'FRA', '250', ('France')),
('GF', 'GUF', '254', ('French Guiana')),
('PF', 'PYF', '258', ('French Polynesia')),
('TF', 'ATF', '260', ('French Southern and Antarctic Lands')),
('GA', 'GAB', '266', ('Gabon')), ('GM', 'GMB', '270', ('Gambia')),
('GE', 'GEO', '268', ('Georgia')), ('DE', 'DEU', '276', ('Germany')),
('GH', 'GHA', '288', ('Ghana')), ('GI', 'GIB', '292', ('Gibraltar')),
('GR', 'GRC', '300', ('Greece')), ('GL', 'GRL', '304', ('Greenland')),
('GD', 'GRD', '308', ('Grenada')), ('GP', 'GLP', '312', ('Guadeloupe')),
('GU', 'GUM', '316', ('Guam')), ('GT', 'GTM', '320', ('Guatemala')),
('GG', 'GGY', '831', ('Guernsey')), ('GN', 'GIN', '324', ('Guinea')),
('GW', 'GNB', '624', ('Guinea-Bissau')), ('GY', 'GUY', '328', ('Guyana')),
('HT', 'HTI', '332', ('Haiti')),
('HM', 'HMD', '334', ('Heard Island and McDonald Islands')),
('VA', 'VAT', '336', ('Vatican City Holy See')),
('HN', 'HND', '340', ('Honduras')), ('HK', 'HKG', '344', ('Hong Kong')),
('HU', 'HUN', '348', ('Hungary')), ('IS', 'ISL', '352', ('Iceland')),
('IN', 'IND', '356', ('India')), ('ID', 'IDN', '360', ('Indonesia')),
('IE', 'IRL', '372', ('Ireland')), ('IM', 'IMN', '833', ('Isle of Man')),
('IL', 'ISR', '376', ('Israel')), ('IT', 'ITA', '380', ('Italy')),
('JM', 'JAM', '388', ('Jamaica')), ('JP', 'JPN', '392', ('Japan')),
('JE', 'JEY', '832', ('Jersey')), ('JO', 'JOR', '400', ('Jordan')),
('KZ', 'KAZ', '398', ('Kazakhstan')), ('KE', 'KEN', '404', ('Kenya')),
('KI', 'KIR', '296', ('Kiribati')), ('KR', 'KOR', '410', ('South Korea')),
('KW', 'KWT', '414', ('Kuwait')), ('KG', 'KGZ', '417', ('Kyrgyzstan')),
('LA', 'LAO', '418', ('Laos Lao')), ('LV', 'LVA', '428', ('Latvia')),
('LB', 'LBN', '422', ('Lebanon')), ('LS', 'LSO', '426', ('Lesotho')),
('LY', 'LBY', '434', ('Libya Libyan Arab Jamahiriya')),
('LI', 'LIE', '438', ('Liechtenstein')), ('LT', 'LTU', '440', ('Lithuania')),
('LU', 'LUX', '442', ('Luxembourg')), ('MO', 'MAC', '446', ('Macau Macao')),
('MK', 'MKD', '807', ('Macedonia')), ('MG', 'MDG', '450', ('Madagascar')),
('MW', 'MWI', '454', ('Malawi')), ('MY', 'MYS', '458', ('Malaysia')),
('MV', 'MDV', '462', ('Maldives')), ('ML', 'MLI', '466', ('Mali')),
('MT', 'MLT', '470', ('Malta')), ('MH', 'MHL', '584', ('Marshall Islands')),
('MQ', 'MTQ', '474', ('Martinique')), ('MR', 'MRT', '478', ('Mauritania')),
('MU', 'MUS', '480', ('Mauritius')), ('YT', 'MYT', '175', ('Mayotte')),
('MX', 'MEX', '484', ('Mexico')), ('FM', 'FSM', '583', ('Micronesia')),
('MD', 'MDA', '498', ('Moldova')), ('MC', 'MCO', '492', ('Monaco')),
('MN', 'MNG', '496', ('Mongolia')), ('ME', 'MNE', '499', ('Montenegro')),
('MS', 'MSR', '500', ('Montserrat')), ('MA', 'MAR', '504', ('Morocco')),
('MZ', 'MOZ', '508', ('Mozambique')), ('MM', 'MMR', '104', ('Myanmar')),
('NA', 'NAM', '516', ('Namibia')), ('NR', 'NRU', '520', ('Nauru')),
('NP', 'NPL', '524', ('Nepal')), ('NL', 'NLD', '528', ('Netherlands')),
('AN', 'ANT', '530', ('Netherlands Antilles')),
('NC', 'NCL', '540', ('New Caledonia')), ('NZ', 'NZL', '554', ('New Zealand')),
('NI', 'NIC', '558', ('Nicaragua')), ('NE', 'NER', '562', ('Niger')),
('NG', 'NGA', '566', ('Nigeria')), ('NU', 'NIU', '570', ('Niue')),
('NF', 'NFK', '574', ('Norfolk Island Norfolk Island')),
('MP', 'MNP', '580', ('Northern Mariana Islands')),
('NO', 'NOR', '578', ('Norway')), ('OM', 'OMN', '512', ('Oman')),
('PK', 'PAK', '586', ('Pakistan')), ('PW', 'PLW', '585', ('Palau')),
('PS', 'PSE', '275', ('Palestinian Territory')),
('PA', 'PAN', '591', ('Panama')), ('PG', 'PNG', '598', ('Papua New Guinea')),
('PY', 'PRY', '600', ('Paraguay')), ('PE', 'PER', '604', ('Peru')),
('PH', 'PHL', '608', ('Philippines')),
('PN', 'PCN', '612', ('Pitcairn Islands')), ('PL', 'POL', '616', ('Poland')),
('PT', 'PRT', '620', ('Portugal')), ('PR', 'PRI', '630', ('Puerto Rico')),
('QA', 'QAT', '634', ('Qatar')), ('RE', 'REU', '638', ('Reunion')),
('RO', 'ROU', '642', ('Romania')), ('RU', 'RUS', '643', ('Russia')),
('RW', 'RWA', '646', ('Rwanda')), ('SH', 'SHN', '654', ('Saint Helena')),
('KN', 'KNA', '659', ('Saint Kitts and Nevis')),
('LC', 'LCA', '662', ('Saint Lucia')),
('PM', 'SPM', '666', ('Saint Pierre and Miquelon')),
('VC', 'VCT', '670', ('Saint Vincent and the Grenadines')),
('WS', 'WSM', '882', ('Samoa')), ('SM', 'SMR', '674', ('San Marino')),
('ST', 'STP', '678', ('Sao Tome and Principe')),
('SA', 'SAU', '682', ('Saudi Arabia')), ('SN', 'SEN', '686', ('Senegal')),
('RS', 'SRB', '688', ('Serbia')), ('SC', 'SYC', '690', ('Seychelles')),
('SL', 'SLE', '694', ('Sierra Leone')), ('SG', 'SGP', '702', ('Singapore')),
('SK', 'SVK', '703', ('Slovakia')), ('SI', 'SVN', '705', ('Slovenia')),
('SB', 'SLB', '090', ('Solomon Islands')),
('ZA', 'ZAF', '710', ('South Africa')),
('GS', 'SGS', '239', ('South Georgia and the South Sandwich Islands')),
('ES', 'ESP', '724', ('Spain')), ('LK', 'LKA', '144', ('Sri Lanka')),
('SR', 'SUR', '740', ('Suriname')),
('SJ', 'SJM', '744', ('Svalbard and Jan Mayen')),
('SZ', 'SWZ', '748', ('Swaziland')), ('SE', 'SWE', '752', ('Sweden')),
('CH', 'CHE', '756', ('Switzerland')), ('TW', 'TWN', '158', ('Taiwan')),
('TJ', 'TJK', '762', ('Tajikistan')), ('TZ', 'TZA', '834', ('Tanzania')),
('TH', 'THA', '764', ('Thailand')), ('TL', 'TLS', '626', ('East Timor')),
('TG', 'TGO', '768', ('Togo')), ('TK', 'TKL', '772', ('Tokelau')),
('TO', 'TON', '776', ('Tonga')), ('TT', 'TTO', '780', ('Trinidad and Tobago')),
('TN', 'TUN', '788', ('Tunisia')), ('TR', 'TUR', '792', ('Turkey')),
('TM', 'TKM', '795', ('Turkmenistan')),
('TC', 'TCA', '796', ('Turks and Caicos Islands')),
('TV', 'TUV', '798', ('Tuvalu')), ('UG', 'UGA', '800', ('Uganda')),
('UA', 'UKR', '804', ('Ukraine')),
('AE', 'ARE', '784', ('United Arab Emirates')),
('GB', 'GBR', '826', ('United Kingdom')),
('US', 'USA', '840', ('United States')),
('UM', 'UMI', '581', ('United States Minor Outlying Islands')),
('UY', 'URY', '858', ('Uruguay')), ('UZ', 'UZB', '860', ('Uzbekistan')),
('VU', 'VUT', '548', ('Vanuatu')), ('VE', 'VEN', '862', ('Venezuela')),
('VN', 'VNM', '704', ('Vietnam Viet Nam')),
('VG', 'VGB', '092', ('British Virgin Islands')),
('VI', 'VIR', '850', ('United States Virgin Islands')),
('WF', 'WLF', '876', ('Wallis and Futuna')),
('EH', 'ESH', '732', ('Western Sahara')), ('YE', 'YEM', '887', ('Yemen')),
('ZR', 'ZRR', '', ('Zaire')), ('ZM', 'ZMB', '894', ('Zambia')),)

country_items = (("AF", "Afghanistan"),("AX", "Aland Islands"),("AL", "Albania"),("DZ", "Algeria"),("AS", "American Samoa"),("AD", "Andorra"),("AO", "Angola"),("AI", "Anguilla"),("AQ", "Antarctica"),("AG", "Antigua and Barbuda"),("AR", "Argentina"),("AM", "Armenia"),("AW", "Aruba"),("AU", "Australia"),("AT", "Austria"),("AZ", "Azerbaijan"),("BS", "Bahamas"),("BH", "Bahrain"),("BD", "Bangladesh"),("BB", "Barbados"),("BE", "Belgium"),("BZ", "Belize"),("BJ", "Benin"),("BM", "Bermuda"),("BT", "Bhutan"),("BO", "Bolivia"),("BA", "Bosnia and Herzegovina"),("BW", "Botswana"),("BV", "Bouvet Island"),("BR", "Brazil"),("IO", "British Indian Ocean Territory"),("BN", "Brunei Darussalam"),("BG", "Bulgaria"),("BF", "Burkina Faso"),("BI", "Burundi"),("KH", "Cambodia"),("CM", "Cameroon"),("CA", "Canada"),("CV", "Cape Verde"),("KY", "Cayman Islands"),("CF", "Central African Republic"),("TD", "Chad"),("CL", "Chile"),("CN", "China"),("CX", "Christmas Island"),("CC", "Cocos (Keeling) Islands"),("CO", "Colombia"),("KM", "Comoros"),("CD", "Congo, The Democratic Republic of the"),("CK", "Cook Islands"),("CR", "Costa Rica"),("CI", "Cote d'Ivoire"),("HR", "Croatia"),("CY", "Cyprus"),("CZ", "Czech Republic"),("DK", "Denmark"),("DJ", "Djibouti"),("DM", "Dominica"),("DO", "Dominican Republic"),("EC", "Ecuador"),("EG", "Egypt"),("SV", "El Salvador"),("GQ", "Equatorial Guinea"),("ER", "Eritrea"),("EE", "Estonia"),("ET", "Ethiopia"),("FK", "Falkland Islands (Malvinas)"),("FO", "Faroe Islands"),("FJ", "Fiji"),("FI", "Finland"),("FR", "France"),("GF", "French Guiana"),("PF", "French Polynesia"),("TF", "French Southern Territories"),("GA", "Gabon"),("GM", "Gambia"),("GE", "Georgia"),("DE", "Germany"),("GH", "Ghana"),("GI", "Gibraltar"),("GR", "Greece"),("GL", "Greenland"),("GD", "Grenada"),("GP", "Guadeloupe"),("GU", "Guam"),("GT", "Guatemala"),("GG", "Guernsey"),("GN", "Guinea"),("GW", "Guinea-Bissau"),("GY", "Guyana"),("HT", "Haiti"),("HM", "Heard Island and McDonald Islands"),("VA", "Holy See (Vatican City State)"),("HN", "Honduras"),("HK", "Hong Kong"),("HU", "Hungary"),("IS", "Iceland"),("IN", "India"),("ID", "Indonesia"),("IE", "Ireland"),("IM", "Isle of Man"),("IL", "Israel"),("IT", "Italy"),("JM", "Jamaica"),("JP", "Japan"),("JE", "Jersey"),("JO", "Jordan"),("KZ", "Kazakhstan"),("KE", "Kenya"),("KI", "Kiribati"),("KR", "Korea, Republic of"),("KW", "Kuwait"),("KG", "Kyrgyzstan"),("LA", "Lao People's Democratic Republic"),("LV", "Latvia"),("LB", "Lebanon"),("LS", "Lesotho"),("LY", "Libyan Arab Jamahiriya"),("LI", "Liechtenstein"),("LT", "Lithuania"),("LU", "Luxembourg"),("MO", "Macao"),("MK", "Macedonia, The Former Yugoslav Republic of"),("MG", "Madagascar"),("MW", "Malawi"),("MY", "Malaysia"),("MV", "Maldives"),("ML", "Mali"),("MT", "Malta"),("MH", "Marshall Islands"),("MQ", "Martinique"),("MR", "Mauritania"),("MU", "Mauritius"),("YT", "Mayotte"),("MX", "Mexico"),("FM", "Micronesia, Federated States of"),("MD", "Moldova, Republic of"),("MC", "Monaco"),("MN", "Mongolia"),("ME", "Montenegro"),("MS", "Montserrat"),("MA", "Morocco"),("MZ", "Mozambique"),("MM", "Myanmar"),("NA", "Namibia"),("NR", "Nauru"),("NP", "Nepal"),("NL", "Netherlands"),("AN", "Netherlands Antilles"),("NC", "New Caledonia"),("NZ", "New Zealand"),("NI", "Nicaragua"),("NE", "Niger"),("NG", "Nigeria"),("NU", "Niue"),("NF", "Norfolk Island"),("MP", "Northern Mariana Islands"),("NO", "Norway"),("OM", "Oman"),("PK", "Pakistan"),("PW", "Palau"),("PS", "Palestinian Territory, Occupied"),("PA", "Panama"),("PG", "Papua New Guinea"),("PY", "Paraguay"),("PE", "Peru"),("PH", "Philippines"),("PN", "Pitcairn"),("PL", "Poland"),("PT", "Portugal"),("PR", "Puerto Rico"),("QA", "Qatar"),("RE", "Reunion"),("RO", "Romania"),("RU", "Russian Federation"),("RW", "Rwanda"),("SH", "Saint Helena"),("KN", "Saint Kitts and Nevis"),("LC", "Saint Lucia"),("PM", "Saint Pierre and Miquelon"),("VC", "Saint Vincent and the Grenadines"),("WS", "Samoa"),("SM", "San Marino"),("ST", "Sao Tome and Principe"),("SA", "Saudi Arabia"),("SN", "Senegal"),("RS", "Serbia"),("SC", "Seychelles"),("SL", "Sierra Leone"),("SG", "Singapore"),("SK", "Slovakia"),("SI", "Slovenia"),("SB", "Solomon Islands"),("ZA", "South Africa"),("GS", "South Georgia and the South Sandwich Islands"),("ES", "Spain"),("LK", "Sri Lanka"),("SR", "Suriname"),("SJ", "Svalbard and Jan Mayen"),("SZ", "Swaziland"),("SE", "Sweden"),("CH", "Switzerland"),("TW", "Taiwan, Province of China"),("TJ", "Tajikistan"),("TZ", "Tanzania, United Republic of"),("TH", "Thailand"),("TL", "Timor-Leste"),("TG", "Togo"),("TK", "Tokelau"),("TO", "Tonga"),("TT", "Trinidad and Tobago"),("TN", "Tunisia"),("TR", "Turkey"),("TM", "Turkmenistan"),("TC", "Turks and Caicos Islands"),("TV", "Tuvalu"),("UG", "Uganda"),("UA", "Ukraine"),("AE", "United Arab Emirates"),("GB", "United Kingdom"),("US", "United States"),("UM", "United States Minor Outlying Islands"),("UY", "Uruguay"),("UZ", "Uzbekistan"),("VU", "Vanuatu"),("VE", "Venezuela, Bolivarian Republic of"),("VN", "Viet Nam"),("VG", "Virgin Islands, British"),("VI", "Virgin Islands, U.S."),("WF", "Wallis and Futuna"),("EH", "Western Sahara"),("YE", "Yemen"),("ZM", "Zambia"),)
short_country_items = [(x, y[:30]) for x,y in country_items]

iso_country_items = [(country_2digit_to_iso(country2), name) for country2, name
                     in country_items]

clean_countries = ['AW', 'AU', 'AT', 'BE', 'BR', 'VG', 'BN', 'CA', 'KY', 'CY',
                   'DK', 'GQ', 'FK', 'FO', 'FI', 'FR', 'PF', 'DE', 'GI', 'GR',
                   'GL', 'GG', 'HK', 'IS', 'IE', 'IM', 'IL', 'IT', 'JP', 'JE',
                   'KW', 'LI', 'LU', 'MO', 'NL', 'AN', 'NZ', 'NO', 'PT', 'PR',
                   'QA', 'SM', 'SG', 'SI', 'KR', 'ES', 'SE', 'CH', 'BS', 'AE',
                   'GB', 'US', 'UM', 'VI']

clean_country_iso_items = [(country_2digit_to_iso(x), country_2digit_to_name(x))
                           for x in clean_countries]


