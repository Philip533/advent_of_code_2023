program main
  use iso_fortran_env, only : int64, real64
  implicit none

  integer, dimension(4) :: times, dist
  character(len=255), dimension(4) :: times_char, dist_char
  character(len=255) :: big_t, big_d
  integer(int64) :: full_d, full_t
  character(len=:), allocatable :: trim_t, trim_d

  real :: distance

  integer :: i, counter = 0, j, prod = 1

  ! Open the file
  open(18, file="input")

  ! Read the times and distances
  read(18,*) times
  read(18,*) dist

  ! Do part 1
  counter = 0
  do j = 1, 4
  do i = 1, times(j)
    distance = i*(times(j) - i)
    if(distance > dist(j)) then
      counter = counter + 1
    end if
  end do

  prod = prod*counter
  counter = 0
  end do

  ! Force times and distances into characters
  do i = 1, 4
    write(times_char(i), *) times(i)
    write(dist_char(i), *) dist(i)
  end do

  ! Concatenate for the second part of the question
  big_t = &
  trim(adjustl(times_char(1)))//trim(adjustl(times_char(2)))//trim(adjustl(times_char(3)))//trim(adjustl(times_char(4)))
  big_d = trim(adjustl(dist_char(1)))//trim(adjustl(dist_char(2)))//trim(adjustl(dist_char(3)))//trim(adjustl(dist_char(4)))
  trim_t = trim(adjustl(big_t))
  trim_d = trim(adjustl(big_d))
  read(trim_t, *) full_t
  read(trim_d, *) full_d

  do i = 1, full_t
    distance = i*(full_t - i)
    if(distance > full_d) then
      counter = counter + 1
    end if
  end do

  print *, "Part 1 solution = ", prod
  print *, "Part 2 solution = ", counter
end program main
