Feature: Commandline Options
    In order to specify the behaviour of the program
    As a user
    The program should use command line options

    Scenario Outline: Blenders
        Given I enter <argument> to the program,
            when I run the program
            then it should run <function>

        Examples: Modes
            | thing         | other thing |
            | Red Tree Frog | mush        |

        Examples: Consumer Electronics
            | thing         | other thing |
            | iPhone        | toxic waste |
            | Galaxy Nexus  | toxic waste |

