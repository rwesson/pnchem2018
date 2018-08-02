FC=gfortran
LD=gfortran
FFLAGS=-ffree-line-length-0 -O3 -fno-backtrace
FFLAGS=-Wall

.PHONY: clean new

distrib: source/distrib.o
	$(LD) $(FFLAGS) -o $@ $^

%.o: %.f90
	$(FC) $(FFLAGS) $< -c -o $@

clean:
	rm -f distrib source/*.o source/*.mod

new: clean distrib
