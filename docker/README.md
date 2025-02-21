# Running Emerald using Docker instances

You can find a Docker instance with Emerald installed at
[`portoleks/in5570v25`](https://hub.docker.com/r/portoleks/in5570v25).

This is the fastest way to get Emerald to run on your machine.

## Environment

You can compile and run emerald programs from with in the Docker image.
To do so, type in the command

```bash
$ make environment
```

You can exit the instance by typing `Ctrl-D`, or by running the program

```bash
$ exit
```

from within the instance.

## Compiling

Inside the instance, the programs `ec` and `emx` will be available.
The former compiles an emerald file with the extension `.m` into a
`.x` file which can be run using the latter.

## Testing Kilroy

First, make sure that you have the latest version of the image:

```
$ docker pull portoleks/in5570v25
```

Next, navigate to **this** directory, containing our `Makefile`. You
can start an instance of the Docker image using the `make environment`
target. You will be greeted with something like:

```
$ make environment
195c51361521@172.17.0.2 ~/src
$
```

`195c51361521@172.17.0.2` is a descriptor of the Docker image, with
the image tag on the left, and the IP address on the right.  If for
some reason you do not see the IP address (most likely because you
forgot to pull the latest version of `portoleks/in5570v25`), then you
can use `hostname -I` to find it:

```
195c51361521@172.17.0.2 ~/src
$ hostname -I
172.17.0.2 # Here it is!
195c51361521@172.17.0.2 ~/src
$
```

Place a `kilroy.m` in **this** directory (or create a special folder
for `oblig1`, and place it there). **This** directory will be volume
mounted into the Docker container when you do `make environment`,
meaning you will get a mirror of this directory inside the container
under `/home/docker/src`.

You shouldn't need to restart the Docker container, since volume
mounted directories are continuously mirrored. We can now use `ec` to
compile `kilroy.m` to get `kilroy.x`:

```
195c51361521@172.17.0.2 ~/src
$ ec kilroy.m
Compiling kilroy.m # All looks well here!
195c51361521@172.17.0.2 ~/src
$ ls
Makefile  README.md  kilroy.m  kilroy.x
```

Now, start an Emerald node, which will serve as the root node:

```
195c51361521@172.17.0.2 ~/src
$ emx -R
Emerald listening on port 17099 42cb, epoch 6265 1879
```

Hence, an Emerald node will be available at `172.17.0.2:17099`. **Do
not** exit this terminal. If you do, the Emerald node will fall.

Now, start another container in another terminal:

```
$ make environment
bbe85a0bc212@172.17.0.3 ~/src
```

And execute `kilroy.x with the above node as the root node:

```
bbe85a0bc212@172.17.0.3 ~/src
$ emx -R172.17.0.2:17099 kilroy.x
Emerald listening on port 17099 42cb, epoch 65255 fee7
Starting at 1120665319
Comming over. Kind regards, Kilroy
I am done
```

If all is working as intended, you will also see the following message
in the terminal of the root node:

```
Comming over. Kind regards, Kilroy
```
