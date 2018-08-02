program distrib

! generate 152 values of adf

! for all objects, take a value from distribution derived from HII regions - mean 1.9, sd 0.5
! for 20%, add a value from log normal distrib with mean 1.0 and sd 0.5

implicit none
integer :: i
real :: r_uniform,gaussian,adf

open(110,file="synthetic_hii")

do i=1,54

  adf=0.45*gaussian()+1.92
  write(110,*) adf

enddo

close(110)
open(110,file="synthetic_pne")

do i=1,152

  adf=gaussian()*0.45+2.0
  call random_number(r_uniform)

  if (r_uniform>0.5) then
    adf=adf+10**(0.9*gaussian()+0.6)
  endif

  write(110,*) adf

enddo

end program distrib

real function gaussian()

REAL     :: s = 0.449871, t = -0.386595, a = 0.19600, b = 0.25472,           &
            r1 = 0.27597, r2 = 0.27846, u, v, x, y, q

  do
    call random_number(u)
    call random_number(v)
    v = 1.7156 * (v - 0.5)
    x = u - s
    y = abs(v) - t
    q = x**2 + y*(a*y - b*x)
    if (q .lt. r1) exit
    if (q .gt. r2) cycle
    if (v**2 .lt. -4.0*log(u)*u**2) exit
  enddo
  gaussian = v/u

  return

end function gaussian
