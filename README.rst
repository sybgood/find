       -executable
              Matches files which are executable and directories which are
              searchable (in a file name resolution sense) by the current
              user.  This takes into account access control lists and other
              permissions artefacts which the -perm test ignores.  This test
              makes use of the access(2) system call, and so can be fooled
              by NFS servers which do UID mapping (or root-squashing), since
              many systems implement access(2) in the client's kernel and so
              cannot make use of the UID mapping information held on the
              server.  Because this test is based only on the result of the
              access(2) system call, there is no guarantee that a file for
              which this test succeeds can actually be executed.

       -gid n File's numeric group ID is n.

       -iname pattern
              Like -name, but the match is case insensitive.  For example,
              the patterns `fo*' and `F??' match the file names `Foo',
              `FOO', `foo', `fOo', etc.  The pattern `*foo*` will also match
              a file called '.foobar'.
       -NAME         top
       find - search for files in a directory hierarchy
