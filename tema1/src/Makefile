
all: biseccion-test1.out puntofijo-test1.out newton-test1.out\
	 secante-test1.out regula_falsi-test1.out

biseccion-test1.out: biseccion.py biseccion-test1.py
	./run-test.py $^ > $@

puntofijo-test1.out: puntofijo.py puntofijo-test1.py
	./run-test.py $^ > $@

newton-test1.out: newton.py newton-test1.py
	./run-test.py $^ > $@

secante-test1.out: secante.py secante-test1.py
	./run-test.py $^ > $@

regula_falsi-test1.out: regula_falsi.py regula_falsi-test1.py
	./run-test.py $^ > $@