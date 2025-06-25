module subroutines

    use settings

    implicit none

    contains

    !##########################################
    ! Initialisation of the particles (random)
    !##########################################

    subroutine init_part(pos, vel)
        real(kind=dp), intent(inout) :: pos(3, n), vel(3, n)
        integer :: i
        real(kind=dp) :: x, y, z, r
        real(kind=dp), parameter :: omega=1.223_dp

        do i=1, n

            ! Initialize positions
            r = 2

            do while (r > 1.0)
                call random_number(x)
                call random_number(y)
                call random_number(z)
                x = 1-2*x
                y = 1-2*y
                z = 1-2*z
                r = (x**2 + y**2 + z**2)**0.5
            end do
            
            pos(1, i) = x
            pos(2, i) = y
            pos(3, i) = z

            ! Initialize velocities based on solid rotation
            vel(1, i) = -pos(2, i)*omega
            vel(2, i) = pos(1, i)*omega
            vel(3, i) = 0

        end do

        open(unit=300, file='pos.dat', action='write')
        do i=1, n
            write(300, *) pos(1, i), pos(2, i), pos(3, i)
        end do
        close(300)

    end subroutine init_part

    !###############################################
    ! Initialisation of the particles (from a file)
    !###############################################
    subroutine init_part_file(pos, vel)
        real(kind=dp), intent(inout) :: pos(3, n), vel(3, n)
        integer :: i

        open(200, file = init_file, action = 'read')

        do i=1, n
            read(200, *) pos(1, i), pos(2, i), pos(3, i)
        
            vel(1, i) = -pos(2, i)
            vel(2, i) = pos(1, i)
            vel(3, i) = 0
        end do

        close(200)

    end subroutine init_part_file


    !###########################################
    !           Compute accelerations
    !###########################################
    subroutine accel(pos, acc, ep)
        real(kind=dp), intent(in) :: pos(3, n)
        real(kind=dp), intent(out) :: acc(3, n), ep
        real(kind=dp) :: x, y, z, r, ax, ay, az
        integer :: i, j

        ep = 0

        do i=1, n
            acc(1, i) = 0
            acc(2, i) = 0
            acc(3, i) = 0
            
            do j=1, n
                if (j==i) then
                    cycle
                end if
 
                x = pos(1, j) - pos(1, i)
                y = pos(2, j) - pos(2, i)
                z = pos(3, j) - pos(3, i)

                r = sqrt(x**2 + y**2 + z**2 + epsilon**2)

                ax = (gg*m/r**3)*x
                ay = (gg*m/r**3)*y
                az = (gg*m/r**3)*z

                acc(1, i) = acc(1, i) + ax
                acc(2, i) = acc(2, i) + ay
                acc(3, i) = acc(3, i) + az

                ! Compute the potential energy
                ep = ep - 0.5*gg*m**2/r

            end do
        end do

    end subroutine accel


    !###########################################
    !            Leapfrog integrator
    !###########################################
    subroutine leapfrog(pos, vel, acc)
        real(kind=dp), intent(inout) :: pos(3, n), vel(3, n), acc(3, n)
        real (kind=dp) :: acc_new(3, n), ec, ep, Ltot, L0(3)
        integer :: i

        ec = 0

        ! Update positions
        do i=1, n
            pos(1, i) = pos(1, i) + vel(1, i)*dt + 0.5*acc(1, i)*dt**2
            pos(2, i) = pos(2, i) + vel(2, i)*dt + 0.5*acc(2, i)*dt**2
            pos(3, i) = pos(3, i) + vel(3, i)*dt + 0.5*acc(3, i)*dt**2
        end do

        ! Compute new accelerations
        call accel(pos, acc_new, ep)

        ! Update velocities
        do i=1, n
            vel(1, i) = vel(1, i) + 0.5*(acc(1, i) + acc_new(1, i))*dt
            vel(2, i) = vel(2, i) + 0.5*(acc(2, i) + acc_new(2, i))*dt
            vel(3, i) = vel(3, i) + 0.5*(acc(3, i) + acc_new(3, i))*dt
        end do

        ! Update current accelerations and compute kinetic energy
        do i=1, n
            acc(1, i) = acc_new(1, i)
            acc(2, i) = acc_new(2, i)
            acc(3, i) = acc_new(3, i)
            ec = ec + vel(1, i)**2 + vel(2, i)**2 + vel(3, i)**2
        end do

        ! Calculate the total angular momentum
        L0 = [0.0_dp, 0.0_dp, 0.0_dp]
        do i=1,n
            L0(1) = L0(1) + m*(pos(2, i)*vel(3, i) - pos(3, i)*vel(2, i))
            L0(2) = L0(2) + m*(pos(3, i)*vel(1, i) - pos(1, i)*vel(3, i))
            L0(3) = L0(3) + m*(pos(1, i)*vel(2, i) - pos(2, i)*vel(1, i))
        end do
        Ltot = sqrt(L0(1)**2 + L0(2)**2 + L0(3)**2)

        ! Save kinetic, potential energies and total angular momentum
        write(100, *) ep, ec*0.5*m, Ltot

    end subroutine leapfrog

    !###########################################
    !         Evolution of the system
    !###########################################
    subroutine evolve(pos, vel, acc)
        real(kind=dp), intent(inout) :: pos(3, n), vel(3, n), acc(3, n)
        real(kind=dp) :: ep
        integer :: i

        ! Files to save the positions and the energies
        open(unit = 10, file = outpos_name, form = 'unformatted', access = 'stream', action = 'write')
        open(unit = 100, file = energ_name, action="write")

        write(10) pos
        call accel(pos, acc, ep)
        
        ! Main loop
        do i=1, nt
            call leapfrog(pos, vel, acc)   
            write(10) pos
            !print*, "step ", i, " done"
        end do

        close(10)
        close(100)

    end subroutine evolve

end module subroutines
