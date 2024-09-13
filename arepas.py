{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww20100\viewh11380\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs38 \cf0 try:\
	agua = float(input(\'93cantidad de agua: \'93))\
	harina = float(input(\'93cantidad de harina: \'93))\
	aceite = float(input(\'93cantidad de aceite: \'93))/16\
	sal = float(input(\'93cantidad de sal: \'93))/16/3\
except ValueError:\
	print(\'93introdujo alg\'fan valor que no es un numero\'94)\
\
bol = agua + harina + sal\
budare = bol + aceite\
\
print(f\'94La arepa final es \{budare\}\'94)\
}