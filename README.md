# ubuntu setup 

this project is supposed to configure an ubuntu from scratch with various possibilities

at the installation you clone the git repository associated with this project and run it

!!! log anything that happened ! 


https://github.com/almatsy159/ubuntu_config

should check installed programs : [git,docker,vscode,wireshark,mysql,compose...]

should run a server ?, an api ? , a socket handler ? => gunicorn , nginx ?

# prod / dev

prod run gunicorn main.py , in dev run (with uv?) srv.py 


should have several script included : 


1. database backup of files (linux_file.py ? applied to tree only dir opt ! excluding a list ? ) (name conlflict => diff)
2. srv.pi (should handle the creation of a project)
3. should run a productivity script (such as in custom but better ) => see custom ! 
see also editdoc.py ! 

4. check on creation/update/deletion of files ?

5. set as desktop ? => overlay over desktop ? => short cut ?

6. math view module ? all curve with successive transformation 
7. css lib 



# run the project 

# create a config.py file 
cp config_example.py

## uv run main.py

