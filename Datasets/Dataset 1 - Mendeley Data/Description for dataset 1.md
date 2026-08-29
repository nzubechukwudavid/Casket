Description

This dataset contains headers of 2157 binary executable samples comprising 1134 legitimate software (goodware) and 1023 ransomware, grouped into 25 ransomware families. The dataset was retrieved by extracting raw information of the PE header (first 1024 bytes).



The CSV file columns are sample ID, filename, target class (GR), family ID, and numerical columns from 0 to 1023, as follows:

&#x09;		| 	ID			| 	filename			| GR	| 	family	| 			0 - 1023					|

Goodware	| 10000 to 11133	| Their name.exe		| 0	| 0			| Numerical features ranging from 0 to 255	|

Ransomware	| 20000 to 21022	| Their SHA-256 hash	| 1	| 25 family IDs	| Numerical features ranging from 0 to 255	|



Family IDs:

Avaddon			1

Babuk			2

Blackmatter		3

Conti			4

Darkside			5

Dharma			6

Doppelpaymer	7

Exorcist			8

Gandcrab		9

Lockbit			10

Makop			11

Maze			12

Mountlocker		13

Nefilim			14

Netwalker		15

Phobos			16

Pysa				17

Ragnarok		18

RansomeXX		19

Revil			20

Ryuk			21

Stop				22

Thanos			23

Wastedlocker		24

Zeppelin			25



A complete description of this dataset can be found in the paper "Moreira, C.C., Moreira, D.C., Sales Jr., C. de S. de:

Improving Ransomware Detection based on Portable Executable Header using Xception Convolutional Neural Network. Computers \& Security, 103265 (2023), DOI: https://doi.org/10.1016/j.cose.2023.103265, URL: https://www.sciencedirect.com/science/article/pii/S016740482300175X "



Please, reference our work when using this dataset.

