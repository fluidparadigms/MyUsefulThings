
module stringythingy
    use, intrinsic :: iso_c_binding
    character(kind=c_char), dimension(1), save, target, private :: dummystring='.'
end module

subroutine printversion()
    use, intrinsic :: iso_c_binding
    implicit none

    character(kind=c_char), dimension(:), pointer :: vers_str_fptr
    type(c_ptr) :: vers_str_cptr
    integer(c_size_t) :: slen

    interface
        function getversionstring(slen) result(vstr) bind(c,name='getvers')
            use, intrinsic :: iso_c_binding
            implicit none
            type(c_ptr) :: vstr
            integer(c_size_t) :: slen
        end function
    end interface

    write(*,*) 'try to print from fortran'

    vers_str_cptr = getversionstring(slen)
    write(*,*) 'string len = ',slen

    call c_f_pointer(fptr=vers_str_fptr, cptr=vers_str_cptr, shape=[slen])

    write(*,*) vers_str_fptr

end subroutine


