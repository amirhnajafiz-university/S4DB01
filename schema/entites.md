# Entities

The list of project entities.

<ul>
    <li>
        User
        <ul>
            <li>
                Username (primary key) :: string
            </li>
            <li>
                Password :: string
            </li>
            <li>
                Name :: string
            </li>
            <li>
                Email :: string
            </li>
            <li>
                Phone number :: string
            </li>
            <li>
                National ID :: string
            </li>
            <li>
                Wallet :: int
            </li>
            <li>
                Point :: int
            </li>
        </ul>
    </li>
    <li>
        Special User (weak entity) extends from User
        <ul>
            <li>
                Pro ID (primary key) :: int
            </li>
            <li>
                Expire date :: date
            </li>
        </ul>
    </li>
    <li>
        Movie
        <ul>
            <li>
                Movie ID (primary key) :: int
            </li>
            <li>
                File :: string
            </li>
            <li>
                Name :: string
            </li>
            <li>
                Creators :: string
            </li>
            <li>
                Year :: int
            </li>
            <li>
                Description :: string
            </li>
        </ul>
    </li>
    <li>
        Special Movie (weak entity) extends from Movie
        <ul>
            <li>
                special movie id (primary key) :: int
            </li>
            <li>
                price :: int
            </li>
        </ul>
    </li>
    <li>
        Admin
        <ul>
            <li>
                username admin (primary key) :: string
            </li>
            <li>
                password :: string
            </li>
        </ul>
    </li>
    <li> 
        Tag (for categories)
        <ul>
            <li>
                tag ID (primary key) :: int
            </li>
            <li>
                name :: string
            </li>
        </ul>
    </li>
    <li>
        List (for listing movies)
        <ul>
            <li>
                list ID (primary key) :: int
            </li>
            <li>
                name :: string
            </li>
            <li>
                description :: string
            </li>
        </ul>
    </li>
</ul>