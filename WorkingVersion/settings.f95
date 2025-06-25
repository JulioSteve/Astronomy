module settings
    implicit none

    ! Precision selector
    integer, public, parameter :: dp = SELECTED_REAL_KIND(P=8)
    
    ! Number of particles
    integer, public, parameter:: n = 5000
    ! Number of time step
    integer, public, parameter :: nt = 3000
    ! Time step
    real(kind=dp), public, parameter :: dt = 0.005

    ! Mass of each particle
    real(kind=dp), public, parameter :: m = 1.0/n

    ! Name of the file to save the positions
    character(len=*), public, parameter :: outpos_name = 'output/position.bin'
    ! Name of the file to save the energies
    character(len=*), public, parameter :: energ_name = 'output/energy.dat'

    ! Choice between initial positions from a file or computed randomly
    logical, public, parameter :: use_init_file = .false.
    ! Name of the file to load the initial positions (not necessary if use_init_file is set to .false.)
    character(len=*), public, parameter :: init_file = 'pos.dat'

    ! Minimal distance between two particles (smoothing lenght)
    real(kind=dp), public, parameter :: epsilon = 0.01

    ! Pi
    real(kind=dp), public, parameter :: pi = acos(-1.0)
    ! Gravitational constant
    real(kind=dp), public, parameter :: gg = 1.

end module settings
