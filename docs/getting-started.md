# Getting Started

# Table of Contents

<!--TOC-->

- [Table of Contents](#table-of-contents)
- [Software Setup](#software-setup)
  - [Introduction](#introduction)
  - [Installation and Setup](#installation-and-setup)
    - [Operating systems](#operating-systems)
    - [Getting the Code](#getting-the-code)
    - [Installing Software Dependencies](#installing-software-dependencies)
    - [Installing an IDE](#installing-an-ide)
      - [Installing an IDE: CLion](#installing-an-ide-clion)
        - [Getting your Student License](#getting-your-student-license)
        - [Installing CLion](#installing-clion)
    - [Installing an IDE: VS Code](#installing-an-ide-vs-code)
    - [Editing with Vim or NeoVim](#editing-with-vim-or-neovim)
  - [Building and Running the Code](#building-and-running-the-code)
    - [Building from the command line](#building-from-the-command-line)
    - [Building from the command line using the fuzzy finder](#building-from-the-command-line-using-the-fuzzy-finder)
    - [Building with CLion](#building-with-clion)
    - [Building with VS Code](#building-with-vs-code)
    - [Running our AI, Simulator, SimulatedTests or Robot Diagnostics](#running-our-ai-simulator-simulatedtests-or-robot-diagnostics)
  - [Debugging](#debugging)
    - [Debugging with CLion](#debugging-with-clion)
    - [Debugging from the Command Line](#debugging-from-the-command-line)
  - [Profiling](#profiling)
    - [Callgrind](#callgrind)
    - [Tracy](#tracy)
  - [Building for the robot](#building-for-the-robot)
  - [Deploying Robot Software to the robot](#deploying-robot-software-to-the-robot)
  - [Testing Robot Software locally](#testing-robot-software-locally)
  - [Setting up Virtual Robocup 2021](#setting-up-virtual-robocup-2021)
    - [Setting up the SSL Simulation Environment](#setting-up-the-ssl-simulation-environment)
- [Workflow](#workflow)
  - [Issue and Project Tracking](#issue-and-project-tracking)
    - [Issues](#issues)
  - [Git Workflow](#git-workflow)
    - [Forking and Branching](#forking-and-branching)
    - [Creating a new Branch](#creating-a-new-branch)
    - [Making Commits](#making-commits)
    - [Updating Your Branch and Resolving Conflicts](#updating-your-branch-and-resolving-conflicts)
    - [Formatting Your Code](#formatting-your-code)
    - [Pull Requests](#pull-requests)
    - [Reviewing Pull Requests](#reviewing-pull-requests)
  - [Example Workflow](#example-workflow)
  - [Testing](#testing)

<!--TOC-->

# Software Setup

## Introduction

These instructions assume that you have the following accounts setup:
- [GitHub](https://github.com/login)
- [Discord](https://discord.com). Please contact a Thunderbots lead to receive the invite link.

These instructions assume you have a basic understanding of Linux and the command line. There are many great tutorials online, such as [LinuxCommand](http://linuxcommand.org/). The most important things you'll need to know are how to move around the filesystem and how to run programs or scripts.

## Installation and Setup

### Operating systems

We currently only support Linux, specifically Ubuntu.

If you have a X86_64 machine, we support Ubuntu 22.04 LTS and Ubuntu 24.04 LTS.

If you have a ARM64 (also known as AARCH64) machine, we support Ubuntu 24.04 LTS.

You are welcome to use a different version or distribution of Linux, but may need to make some tweaks in order for things to work.

You can use Ubuntu 22.04 LTS or Ubuntu 24.04 LTS inside Windows through Windows Subsystem for Linux, by following [this guide](./getting-started-wsl.md). **Running and developing Thunderbots on Windows is experimental and not officially supported.**

### Getting the Code

1. Open a new terminal
2. Install git by running `sudo apt-get install git`
3. Go to the [software repository](https://github.com/UBC-Thunderbots/Software)
4. Click the `Fork` button in the top-right to fork the repository ([click here to learn about Forks](https://help.github.com/en/articles/fork-a-repo))
   1. Click on your user when prompted
   2. You should be automatically redirected to your new fork
5. Clone your fork of the repository. As GitHub is forcing users to stop using usernames and passwords for authorization, we will be using the SSH link. 

   To clone using SSH:

   1. If not setup prior, you will need to add an SSH key to your GitHub account. Instructions can be found [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).  For each computer you contribute to GitHub with, you will need an additional SSH Key pair linked to your account.
   2.  After you have successfully set up a SSH key for your device and added it to GitHub, you can clone the repository using the following command:
        1.  e.g. `git clone git@github.com:<your_username>/Software.git`
        2.  You can find this link under the green `Code` button on the main page of your fork on GitHub, under the SSH tab.  (This should now be available after adding your SSH key to GitHub successfully.)

   Alternatively, you can clone using HTTPS. You'll need to either use a credential helper (Git Credential Manager, GitHub CLI, etc.) or a personal access token ([details here](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls)).
6. Set up your git remotes ([what is a remote and how does it work?](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes))
   1. You should have a remote named `origin` that points to your fork of the repository. Git will have set this up automatically when you cloned your fork in the previous step.
   2. You will need to add a second remote, named `upstream`, that points to our main Software repository, which is where you created your fork from. (**Note:** This is _not_ your fork)
      1. Open a terminal and navigate to the folder you cloned (your fork): `cd path/to/the/repository/Software`
      2. Navigate to our main Software repository in your browser and copy the url from the green `Code` button. Copy the SSH url if you originally cloned with SSH, or use the HTTPS url if you previously cloned with HTTPS
      3. From your terminal, add the new remote by running `git remote add upstream <the url>` (without the angle brackets)
         1. e.g. `git remote add upstream git@github.com:UBC-Thunderbots/Software.git`
      4. That's it. If you want to double check your remotes are set up correctly, run `git remote -v` from your terminal (at the base of the repository folder again). You should see two entries: `origin` with the url for your fork of the repository, and `upstream` with the url for the main repository

*See our [workflow](#workflow) for how to use git to make branches, submit Pull Requests, and track issues*

### Installing Software Dependencies

We have several setup scripts to help you easily install the necessary dependencies in order to build and run our code. You will want to run the following scripts, which can all be found in `Software/environment_setup`

* Inside a terminal, navigate to the environment_setup folder. e.g. `cd path/to/the/repository/Software/environment_setup`
* Run `./setup_software.sh`
  * You will be prompted for your admin password
  * This script will install everything necessary in order to build and run our software 

### Installing an IDE

For those who prefer working on C/C++ with an IDE, we provide two options: CLion for an integrated experience and VS Code for a more lightweight setup. Both support our build system `bazel`.

#### Installing an IDE: CLion

CLion is the most full-featured IDE, with code completion, code navigation, and integrated building, testing, and debugging.

##### Getting your Student License

CLion is free for students, and you can use your UBC alumni email address to create a student account. If you already have a student account with JetBrains, you can skip this step.

1. If you haven't done so already, setup your UBC alumni email account [here](https://id.ubc.ca/).
2. Using your UBC email account, get a JetBrains education account [here](https://www.jetbrains.com/shop/eform/students).
   1. _JetBrains will send an initial email to confirm the UBC email you inputted. Once you have confirmed, another email will be sent to activate your new education account. You will use this account to set up CLion later on._

##### Installing CLion

1. Follow [the latest instructions from JetBrains](https://www.jetbrains.com/help/clion/installation-guide.html#toolbox) on installing CLion. We recommend installing CLion through the JetBrains Toolbox App which makes it easy to upgrade/downgrade your version of CLion if necessary.
2. When you run CLion for the first time, you will be prompted to enter your JetBrains account or License credentials. Use your student account.
3. Install the [Bazel plugin for CLion](https://plugins.jetbrains.com/plugin/9554-bazel-for-clion).

### Installing an IDE: VS Code

VS Code is a more lightweight "IDE", with support for code navigation, code completion, and integrated building and testing. However, debugging isn't integrated by default into VS Code.

1. Follow the [latest instructions from the VS Code documentation](https://code.visualstudio.com/docs/setup/linux) on installing VS Code.
2. Open VS Code. Go to File -> Open Folder and navigate to where you cloned the software repo. So if I cloned the repo to `/home/my_username/Downloads/Software`, I would select `/home/my_username/Downloads/Software`.
3. VS Code will prompt you to install recommended extensions. Click `Install` — this installs necessary plugins to work on the codebase. (Bazel, C++, Python, etc.)
4. Navigate to File -> Preferences -> Settings -> Workspace -> Extensions -> Bazel and select the `Bazel: Enable Code Lens` option.

### Editing with Vim or NeoVim

When editing with Vim or NeoVim, it's helpful to use plugins, such as [COC](https://github.com/neoclide/coc.nvim) or [LSP](https://github.com/neovim/nvim-lspconfig) to find references, go-to-definition, autocompletion, and more.
These tools require a `compile_commands.json` file, which can be generated by following these instructions:
1. Symlink `src/external` to `bazel-out/../../../external`: `ln -s bazel-out/../../../external .` from the src folder
2. Generate the `compile_commands.json` file: `bazel run //:refresh_compile_commands`.


## Building and Running the Code

### Building from the command line

1. Navigate to the root of this repository (wherever you have it cloned on your computer)
2. Navigate to `src`.
3. Build a specific target for running (for example): `bazel build //software/geom:angle_test`
4. Run a specific target by running (for example): `bazel run //software/geom:angle_test`
5. Run a specific *test* by running (for example): `bazel test //software/geom:angle_test`
6. Build everything by running `bazel build //...`
7. Run all the tests by running `bazel test //...`

*See the Bazel [command-line docs](https://bazel.build/reference/command-line-reference) for more info.*
*Note: the targets are defined in the BUILD files in our repo*

### Building from the command line using the fuzzy finder

We have a `tbots.py` test runner script in the src folder that will fuzzy find for targets and call Bazel. For example, 

1. Build a specific target for running (for example): `./tbots.py build angletest`
2. Run a specific target by running (for example): `./tbots.py run goalietactictest -t`
3. Run a specific *test* by running (for example): `./tbots.py test goalietactictest -t`

where the `-t` flag indicates whether Thunderscope should be launched. Run `./tbots.py --help` for more info

### Building with CLion

First, we need to setup CLion:
1. Open CLion
2. Select `Import Bazel Project`
3. Set `Workspace` to wherever you cloned the repository + `/src`. So if I cloned the repo to `/home/my_username/Downloads/Software`, my workspace would be `/home/my_username/Downloads/Software/src`.
4. Select `Import project view file`, and select the file `.bazelproject` (which will be under the `src` folder)
5. Click `Next`
6. Change the Project Name to whatever you want. Leave everything else as it is ("Use shared project view file" should be selected).
7. Click `Finish` and you're good to go! Give CLion some time to find everything in your repo.

Now that you're setup, if you can run it on the command line, you can run it in CLion. There are two main ways of doing so.
1. Open any `BUILD` file and right click on a `cc_library()` call. This will give you the option to `Run` or `Debug` that specific target. Try it by opening `Software/src/software/geom/BUILD` and right-clicking on the `cc_library` for `angle_test`!
2. Add a custom build configuration (more powerful, so make sure you understand this!)
    1. Select `Add Configuration` from the drop-down in the top-right of CLion
    2. Click on `+`, choose `Bazel Command`.
    3. For `Target Expression`, you can put anything that comes after a `build`, `run`, `test`, etc. call on the command line. For example: `//software/geom:angle_test`.
    4. For `Bazel Command` you can put any Bazel command, like `build`, `run`, `test`, etc.
    5. Click `Ok`, then there should be a green arrow in the top right corner by the drop-down menu. Click it and the test will run!

### Building with VS Code

1. Open VS Code
2. Navigate to `Software/src/software/geom/BUILD`
3. On top of every `cc_test`, `cc_library` and `cc_binary` there should be a `Test ...`, `Build ...` or `Run ...` for the respective target.
4. Click `Test //software/geom:angle_test` to run the `angle_test`

### Running our AI, Simulator, SimulatedTests or Robot Diagnostics

1. Run our AI on [Thunderscope](./software-architecture-and-design.md#thunderscope-gui):
    - [Thunderscope](./software-architecture-and-design.md#thunderscope-gui) is the software that coordinates and visualizes our AI, Simulator, and RobotDiagnostics.
    - After launching Thunderscope, we can see what the AI is currently "seeing" and interact with it through dynamic parameters. 
    - If we want to run with simulated AI vs AI:
        - `./tbots.py run thunderscope_main --enable_autoref` will start Thunderscope with a Simulator, a blue FullSystem, yellow FullSystem and a headless Autoref.
        - Each FullSystem contains the respective AI for each side. The command will start Thunderscope and set up communication between the Simulator, Gamecontroller, FullSystems and Autoref.
        - We use ER Force's Simulator to simulate how our robots would behave on the field. This simulator is powerful because it includes vision noise, allowing us to further stress test our gameplay.
        - The Simulator outputs SSL Vision packets, which contain position information of all robots and the ball.
        - The Autoref sends RefereeCommands to both AIs, so that the AIs can respond to game events. If you want to manually send RefereeCommands using the Gamecontroller, omit the `--enable_autoref` flag. If you run `thunderscope_main` with `--enable_autoref --show_autoref_gui` flags, an additional TigersAutoref window shows information about Tigers's filtered vision, obstacles that could result in rules violations and ball speed history.
        - Our AI can now "see" the robots, and they should be displayed on the Visualizer.
        - Currently, there should be six blue robots and six yellow robots on screen. All these robots are probably stationary because there are no RefereeCommands to respond to. We can change this state using the GameController. In Thunderscope, navigate to the "GameController" tab at the top or alternatively, type `localhost:8081` in your browser. Here, we should see the GameController page with two columns of buttons on the left: one representing commands for the Yellow team and one for the Blue team. We can control gameplay by issuing RefereeCommands.
            - To start normal gameplay from Kickoff, press "Stop", then "Kickoff" for either team and then "Normal Start".
            - To learn more about how we coordinate different RefereeCommands to start special case gameplay behaviour (PenaltyKick, CornerKick, FreeKick), look at the [SSL rule documentation](https://ssl.robocup.org/rules/).
        - In addition, you can use ctrl-click to move the ball around in the Simulator, or try changing the Play Override on the Visualizer to select specific Plays!
    
    - If we want to run with one AI and / or Diagnostics
      - `./tbots.py run thunderscope_main [--run_blue | --run_yellow] [--run_diagnostics]` will start Thunderscope
        - `[--run_blue | --run_yellow]` indicate which FullSystem to run
        - `[--run_diagnostics]` indicates if diagnostics should be loaded as well
      - If FullSystem is running, the robots receive input from the AI
      - If Diagnostics is enabled, the robots can also receive input from Manual controls or Xbox controls
      - This mode allows us to test and debug the robots by setting each robot's input to be either AI, Manual Control or Xbox Control
      - Control mode for each robot can be set with each one's drop down menu in the Robot View widget

    - If we want to run it with real robots:
        - Open your terminal, `cd` into `Software/src` and run `ifconfig`.
            - Pick the network interface you would like to use. If you would like to communicate with robots on the network, make sure to select the interface that is connected to the same network as the robots.
            - For example, on a sample machine, the output may look like this:

                ```
                wlp3s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                        ...
                        [omitted]
                        ...

                lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
                        ...
                        [omitted]
                        ...
                ```

            - An appropriate interface we could choose is `wlp3s0`
            - Hint: If you are using a wired connection, the interface will likely start with `e-`. If you are using a WiFi connection, the interface will likely start with `w-`.
        - If we are running the AI as "blue": `./tbots.py run thunderscope_main --interface=[interface_here] --run_blue`
        - If we are running the AI as "yellow": `./tbots.py run thunderscope_main --interface=[interface_here] --run_yellow`
        - `[interface_here]` corresponds to the `ifconfig` interfaces seen in the previous step
            - For instance, a call to run the AI as blue on WiFi could be: `./tbots.py run thunderscope_main --interface=wlp3s0 --run_blue`. This will start Thunderscope and set up communication with robots over the wifi interface. It will also listen for referee and vision messages on the same interface.
        - **Note: You do not need to include the `--interface=[interface_here]` argument!** You can run Thunderscope without it and use the dynamic configuration widget to set the interfaces for communication to send and receive robot, vision and referee messages.
            - If you choose to include `--interface=[interface_here]` argument, Thunderscope will listen for and send robot messages on this port as well as receive vision and referee messages.
            - Using the dynamic configuration widget is recommended at Robocup. To reduce latencies, it is recommended to connect the robot router to the AI computer via ethernet and use a separate ethernet connection to receive vision and referee messages. In this configuration, Thunderscope will need to bind to two different interfaces, each likely starting with a "e-".
            - If you have specified `--run_blue` or `--run_yellow`, navigate to the "Parameters" widget. In "ai_config" > "ai_control_config" > "network_config", you can set the appropriate interface using the dropdowns for robot, vision and referee message communication.
        - This command will set up robot communication and the Unix full system binary context manager. The Unix full system context manager hooks up our AI, Backend and SensorFusion
2. Run AI along with Robot Diagnostics:
    - The Mechanical and Electrical sub-teams use Robot Diagnostics to test specific parts of the Robot.
    - If we want to run with one AI and Diagnostics
        - `./tbots.py run thunderscope_main [--run_blue | --run_yellow] --run_diagnostics --interface=[interface_here]` will start Thunderscope
            - `[--run_blue | --run_yellow]` indicate which FullSystem to run
            - `--run_diagnostics` indicates if diagnostics should be loaded as well
        - Initially, the robots are all connected to the AI and only receive input from it
        - To change the input source for the robot, use the drop-down menu of that robot to change it between None, AI, and Manual
        - None means the robots are receiving no commands
        - More info about Manual control below
        - `--interface=[interface_here]` corresponds to the `ifconfig` interfaces seen in the previous step
            - For instance, a call to run the AI as blue on WiFi could be: `./tbots.py run thunderscope_main --interface=wlp3s0 --run_blue --run_diagnostics`
            - The `--interface` flag is optional. If you do not include it, you can set the interface in the dynamic configuration widget. See above for how to set the interface in the dynamic configuration widget.
3. Run only Diagnostics
    - To run just Diagnostics
        - `./tbots.py run thunderscope --run_diagnostics --interface <network_interface>`
    - Initially, all of the robots are set to 'None' and will not receive any commands
    - For the robot you want to control, choose Manual in its dropdown menu
    - Manual Control
      - When a robot is in Manual control mode, the commands it receives depend on the radio buttons to the top-right
        - Diagnostics Control allows us to use the on-screen sliders and buttons to control the robot
        - Xbox control allows us to use a connected Xbox controller to control the robots
4. Run our SimulatedPlayTests in Thunderscope
    - This will launch the visualizer and simulate AI Plays, allowing us to visually see the robots acting according to their roles.
    1. For legacy C++ tests (#2581) with the visualizer:
        1. First run Thunderscope configured for receiving protobufs over unix sockets correctly: `./tbots.py run thunderscope_main --visualize_cpp_test`
        2. Then run `./tbots.py test [some_target_here] --run_sim_in_realtime`
    2. For PyTests:
        - With the visualizer: `./tbots.py test [some_target_here] -t`
        - Without the visualizer: `./tbots.py test [some_target_here]`
    3. For legacy C++ tests (#2581) without the visualizer:
        - `./tbots.py test [some_target_here]`
5. Run our SimulatedTacticTests in Thunderscope:
    - This will launch the visualizer and simulate an AI Tactic on a single robot
    1. For legacy C++ tests (#2581) with the visualizer:
        - First, run Thunderscope configured for receiving protobufs over unix sockets correctly: `./tbots.py run thunderscope_main --visualize_cpp_test`
        - Then run `./tbots.py test [some_target_here] --run_sim_in_realtime`
    2. For PyTests:
        - With the visualizer: `./tbots.py test [some_target_here] -t`
        - Without the visualizer: `./tbots.py test [some_target_here]`
    3. For legacy C++ tests (#2581) without the visualizer:
        - `./tbots.py test [some_target_here]`

## Debugging

Debugging from the command line is certainly possible, but debugging in a full IDE is *really* nice (plz trust us). 

### Debugging with CLion

Debugging in CLion is as simple as running the above instructions for building CLion, but clicking the little green bug in the top right corner instead of the little green arrow!

### Debugging from the Command Line

To debug from the command line, first you need to build your target with the debugging flag - `bazel build -c dbg //some/target:here`. When the target builds, you should see a path `bazel-bin/<target>`. Copy that path, and run `gdb <path>`. Please see [here](https://www.cs.cmu.edu/~gilpin/tutorial/) for a tutorial on how to use `gdb` if you're not familiar with it. Alternatively, you could do `bazel run -c dbg --run_under="gdb" //some/target:here`, which will run the target in `gdb`. While this is taken directly from the Bazel docs, gdb may sometimes hang when using `--run_under`, so building the target first with debugging flags and running afterwards is preferred.

## Profiling

Profiling is an optimization tool used to identify the time and space used by code, with a detailed breakdown to help identify areas of potential performance improvements. Unfortunately profiling for Bazel targets is not supported in CLion at this time. Hence, the only way to profile our software is via the command line.

### Callgrind

Callgrind is a profiling tool that is part of the Valgrind suite, designed for analyzing program execution and performance with a focus on functional calls and cache usage. It is useful for determining specific functions in the code that may bottleneck performance.

```
bazel run -c dbg --run_under="valgrind --tool=callgrind --callgrind-out-file=/ABSOLUTE/PATH/TO/profile.callgrind" //target/to:run

// Example
bazel run -c dbg --run_under="valgrind --tool=callgrind --callgrind-out-file=/tmp/profile.callgrind" //software/geom:angle_test
```

This will output the file at the _absolute_ path given via the `--callgrind-out-file` argument. This file can then be viewed using `kcachegrind` (example: `kcachegrind /tmp/profile.callgrind`), giving lots of useful information about where time is being spent in the code.

Callgrind requires generating the profile by tracking every single instruction executed by the code. This design adds significant overhead to the runtime performance and significantly slows down the code. Callgrind is appropriate in finding a general sense of bottlenecks in the code but it is difficult to track issues with blocking code and deadlocks.

### Tracy

Tracy is a lightweight, real-time profiler designed for understanding the performance of a system. It offers insights into CPU usage and memory allocations by adding Tracy's markup API.

To run Tracy:
1. If you haven't installed Tracy: `./environment_setup/install_tracy.sh`. Tracy is __very_particular__ about its dependencies!

2. Run the Tracy profiler: `./tbots.py run tracy`

3. Build and run a binary using the `--tracy` flag. Requires Tracy markup symbols to be added to the code:

    1. For `Thunderloop`: `./tbots.py build thunderloop_main --tracy`

    2. For `FullSystem`: `./tbots.py run thunderscope_main --tracy`

Unlike [Callgrind](Callgrind), we can run (and encouraged to run) Tracy with the binary compiled with any and full compiler optimizations. It can provide us a better understanding of the real-time performance of the code.

**Warning**: Bewarned from the Tracy 16.10.2023 manual:
> The captured data is stored in RAM and only written to the disk when the capture finishes. This can result in memory exhaustion when you capture massive amounts of profile data or even in typical usage situations when the capture is performed over a long time. Therefore, the recommended usage pattern is to perform moderate instrumentation of the client code and limit capture time to the strict necessity.

Tracy also samples call stacks. If the profiled binary is run with root permissions, then Tracy can also inspect the kernel stack trace. By default, Thunderloop is run with root permissions but we can profile `unix_full_system` with elevated permissions by following the on-screen instructions by running:

    ./tbots.py run thunderscope_main --tracy --sudo

## Building for the robot

To build for the robot computer, build the target with the `--platforms=//cc_toolchain:robot` flag and the toolchain will automatically build using the ARM toolchain. For example, `bazel build --platforms=//cc_toolchain:robot //software/geom/...`.

## Deploying Robot Software to the robot

We use Ansible to automatically update software running on the robot. [More info here.](useful-robot-commands.md#flashing-the-robots-compute-module) 

To update binaries on a working robot, you can run:

`bazel run //software/embedded/ansible:run_ansible --platforms=//cc_toolchain:robot --//software/embedded:host_platform=<platform> -- --playbook deploy_robot_software.yml --hosts <robot_ip> --ssh_pass <robot_password>`

Where `<platform>` is the robot platform you are deploying to (`PI` or `NANO`), and `<robot_ip>` is the IP address of the robot you are deploying to. The `robot_password` is the password used to login to the `robot` user on the robot.

## Testing Robot Software locally

It is possible to run Thunderloop without having a fully-working robot. Using this mode is useful when testing features that don't require the power board or motors.

1. To run Thunderloop locally on your computer
    1. First, you must ensure that `redis` is installed. Installation instructions can be found [here](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/). The result of these installation directions will likely enable `redis-server` as a service that starts on boot. You may want to run `sudo systemctl disable redis-server` to prevent this.
    2. Next, run the command `redis-server` in a terminal.
    3. Set up the following required REDIS constants by running the following commands in the terminal:
        - `redis-cli set /robot_id "{robot_id}"` where `{robot_id}` is the robot's ID (e.g. `1`, `2`, etc.)
        - `redis-cli set /network_interface "{network_interface}"` where `{network_interface}` is one of the interfaces listed by `ip a`.
        - `redis-cli set /channel_id "{channel_id}"` where `{channel_id}` is the channel id of the robot (e.g. `1`, `2`, etc.)
        - `redis-cli set /kick_coeff "{kick_coeff}"` where `{kick_coeff}` is a calibrated kicking parameter. When running locally, this parameter doesn't matter so `0` is fine.
        - `redis-cli set /kick_constant "{kick_constant}"` where `{kick_constant}` is a calibrated kicking parameter. When running locally, this parameter doesn't matter so `0` is fine.
        - `redis-cli set /chip_pulse_width "{chip_pulse_width}"` where `{chip_pulse_width}` is a calibrated kicking parameter. When running locally, this parameter doesn't matter so `0` is fine.
    4. Now, run Thunderloop with the following command:
        - `bazel run //software/embedded:thunderloop_main --//software/embedded:host_platform=LIMITED`

2. If you have a robot PC that doesn't have proper communication with the power or motor board, you can still run Thunderloop in a limited capacity to test software features (eg. networking).
    1. First, build the Thunderloop binary:
        - `bazel build //software/embedded:thunderloop_main --//software/embedded:host_platform=LIMITED --platforms=//cc_toolchain:robot`
    2. Find the `<robot_ip>` of the robot you want to run Thunderloop on. This guide may help you find the IP address of the robot: [Useful Robot Commands](useful-robot-commands.md#Wifi-Disclaimer).
    3. Copy the binary to the robot:
        - `scp bazel-bin/software/embedded/thunderloop_main robot@<robot_ip>:/home/robot/thunderloop_main`
    4. SSH into the robot using the following command:
        - `ssh robot@<robot_ip>`
    5. Run the Thunderloop binary on the robot:
        - `sudo ./thunderloop_main`

## Setting up Virtual Robocup 2021

### Setting up the SSL Simulation Environment

1. Fork the [SSL-Simulation-Setup](https://github.com/RoboCup-SSL/ssl-simulation-setup) repository.  
2. Clone it.
3. Follow these [instructions](https://github.com/RoboCup-SSL/ssl-simulation-setup/blob/master/Readme.md) to set up and run the repository.

# Workflow

## Issue and Project Tracking

We try keep our issue and project tracking fairly simple to reduce the overhead associated with tracking all the information and to make it easier to follow. If you are unfamiliar with GitHub issues, [this article](https://guides.github.com/features/issues/) gives a good overview.

### Issues

We use issues to keep track of bugs in our system, and new features or enhancements we want to add. When creating a new issue, we have a simple "Task" template that can be filled out. We *strongly* recommend using the template since it provides guiding questions/headings to make sure we have all the necessary information in each issue.

*It is very important to give lots of detail and context when creating an issue. It is best to pretend you are writing the issue for someone who has not worked on the relevant part of the system before, and to leave a good enough explanation that someone with very little prior knowledge could get started. Sometimes issues get worked on many months after they were created, and we don't want to forget exactly what we wanted to do and why.*

In general if you find an issue with the system, first check with others on your team to make sure that this is indeed unintended behavior (you never know), and make sure that an issue has not already been created before you create a new one.  
  
The same goes for feature requests. Just make sure that whatever you want to say doesn't already exist in an issue.

## Git Workflow

### Forking and Branching

In general, we follow the Forking Workflow

* [What it is](https://www.atlassian.com/git/tutorials/comparing-workflows#forking-workflow)
* [How to use it](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
* Instructions on obtaining your own Fork of our repository can be found in the [Getting the Code](#getting-the-code) section.

### Creating a new Branch

For each issue that you work on, you should have a separate branch. This helps keep work organized and separate.

**Branches should always be created from the latest code on the `master` branch of our main Software repository**. If you followed the steps in [Installation and Setup](#installation-and-setup), this will be `upstream/master`. Once this branch is created, you can push it to your fork and update it with commits until it is ready to merge. 

1. Navigate to the base folder of your Software repository: `cd path/to/the/repository/Software`
2. Make git aware of any new changes to `upstream` by running `git fetch upstream`
3. Create a new branch from `upstream/master` by running `git checkout upstream/master` then `git checkout -b your-branch-name`
   
   Our branch naming convention is: `your_name/branch_name` (all lowercase, words separated by underscores). The branch name should be short and descriptive of the work being done on the branch.
   
   **Example:** if you were working on a new navigation system using RRT and your name was "Bob" your branch name might look like: `bob/new_rrt_navigator`

4. You can now commit changes to this branch and push them to your fork with `git push origin your_branch_name` or `git push -u`

<details>
<summary>Aside: Why should you only create branches from <code>upstream/master</code>?</summary>

Because we squash our commits when we merge Pull Requests, a new commit with a new hash will be created, containing the multiple commits from the PR branch. Because the hashes are different, git will not recognize that the squashed commit and the series of commits that are inside the squashed commit contain the same changes, which can result in conflicts.

For example, lets pretend you have _branch A_, which was originally branched from `upstream/master`. You make a few commits and open a Pull Request. While you're waiting for the Pull Request to be reviewed and merged, you create a new branch, _branch B_, from _branch A_ to get a head start on a new feature. Eventually _branch A_ gets merged into `upstream/master`. Now you want to pull the latest changes from `upstream/master` into _branch B_ to make sure you have the latest code. git will treat the squashed commit that was merged from _branch A_'s Pull Request as a new change that needs to be merged, since _branch B_ will not have a commit with the same git hash. But _branch B_ already has these changes because it was created from branch A! This will cause massive merge conflicts that are nearly impossible to resolve cleanly.

tl;dr Always create new branches from upstream/master. Do not create branches from other feature branches.

</details>

### Making Commits

We don't impose any rules for how you should be committing code, just keep the following general guidelines in mind:

1. Commits should represent logical steps in your workflow. Avoid making commits too large, and try keep related changes together
2. Commit messages should give a good idea of the changes made. You don't have to go in-depth with technical details, but no one will know what you've done if your commit message is "fixed broken stuff"
3. Do not commit any non-code files such as images, videos, or generated files.

### Updating Your Branch and Resolving Conflicts

As you are working on your code on your branch and making commits, you'll want to update your branch with the latest code on `upstream/master` to make sure you're working with the latest code. This is important in case someone else merged new code that affects the code you're working on.

To do this, you have 2 options: rebase or merge. [What's the difference?](https://www.atlassian.com/git/tutorials/merging-vs-rebasing). 

Merging is generally recommended, because it is easier to handle conflicts and get stuff working. To merge, simply run `git pull upstream master`.

Rebasing requires more knowledge of git and can cause crazy merge conflicts, so it isn't recommended. You can simply `git pull --rebase upstream master` to rebase your branch onto the latest `upstream/master`. The main benefit of rebasing is that you get a clean, linear commit history; however, we squash all the commits in each PR into a single commit before merging into master, so the extra effort involved in rebasing is somewhat pointless.

If you do rebase or merge and get conflicts, you'll need to resolve them manually. [See here for a quick tutorial on what conflicts are and how to resolve them](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts). Feel free to do this in your IDE or with whatever tool you are most comfortable with. Updating your branch often helps keep conflicts to a minimum, and when they do appear they are usually smaller. Ask for help if you're really stuck!

### Formatting Your Code

We use a variety of code formatters and linters to automatically format our code. Using automatic tools helps keep things consistent across the codebase without developers having to change their personal style as they write. See the [code style guide](code-style-guide.md) for more information on exactly what these tools enforce.

To format the code, from the `Software` directory run `./scripts/lint_and_format.sh`.

We recommend running the formatting script and then committing all your changes, so that your commits can more easily pass CI.

### Pull Requests

Pull Requests give us a chance to run our automated tests and review the code before it gets merged. This helps us make sure our code on `upstream/master` always compiles and is as bug-free as possible.

The code-review process gives us a chance ask questions or suggest improvements regarding a proposed change, so that the code is of the highest possible quality before being merged. It is also a good opportunity for others on the team to see what changes are being made, even if they are not involved in the project.

The Pull Request process usually looks like the following:
 
1. Make sure all the changes you want to make are pushed to a branch on your fork of the repository
2. Make sure you have [updated your branch](#formatting-your-code) and [formatted your code](#updating-your-branch-and-resolving-conflicts). This is to help make sure CI will pass.
3. From the main page of your fork of the Software repository, click on the "code" tab and then on the "branches" tab below.
4. Find the branch you want to open a Pull Request with and click "New Pull Request"
5. Make sure the target (base-fork) is the `UBC-Thunderbots/Software` repository with branch `master`
6. Give your Pull Request a short but descriptive title (the title should reflect the changes)
7. Fill out the Pull Request template. This includes things like a description of the changes, indicating which issues the Pull Request resolves, and indicating what testing has been done.
8. Add reviewers. This should be anyone that worked with you on the changes or is working on something that will be affected by the changes. Add your team lead and a few other members. Around 3-4 reviewers is a good number, but use your best judgement. Remember, these reviews also help give other team members an idea of the changes that are being made even if they aren't working on them.
    1. At least one "Code Owner" will need to review the change in order for it to be merged
9. Click "Create Pull Request"
10. Now the code can be reviewed. Respond to feedback given by your team members and make changes as necessary by pushing additional commits to your branch.
    1. **If you are a reviewer:**
       1. Look over the code, keeping an eye out for typos, bugs, or improper [code style](code-style-guide.md)
       2. If you are having trouble understanding what a certain part of the code is doing, that's a great place to suggest adding additional comments!
       3. Remember you are critiquing someone's work. Give useful, constructive feedback and justify your thoughts, and don't be mean or degrading. Try to provide a suggested solution where possible.
       4. During re-reviews (Pull Requests typically involve several rounds of changes and review), **it is your responsibility to check that previously requested changes were made and mark the relevant discussions as "resolved"**. "Unresolved" discussions make a great checklist of things to check during a re-review.
       5. Mark the Pull Request as "Approved" when you think it looks good
    2. **If you are the recipient of the review (the PR creator):**
       1. **Make sure to reply to the PR comments as you address / fix issues**. This helps the reviewers know you have made a change without having to go check the code diffs to see if you made a change.
          1. e.g. Reply with "done" or "fixed" to comments as you address them
          2. Leave comments unresolved, let the reviewer resolve them.
       2. Don't be afraid to ask for clarification regarding changes or suggest alternatives if you don't agree with what was suggested. The reviewers and reviewee should work together to come up with the best solution.
       3. **Do not resolve conversations as you address them** (but make sure to leave a comment as mentioned above). That is the responsibility of the reviewers.
       4. Once you have addressed all the comments, re-request review from reviewers.
11. Make sure our automated tests with Github Actions are passing. There will be an indicator near the bottom of the Pull Request. If something fails, you can click on the links provided to get more information and debug the problems.
12. Once your Pull Request has been approved and the automated tests pass, you can merge the code. There will be a big 'merge" button at the bottom of the Pull Request with several options to choose from
    1. We only allow "Squash and merge". This is because it keeps the commit history on `upstream/master` shorter and cleaner, without losing any context from the commit messages (since they are combined in the squashed commit. A squashed commit also makes it easier to revert and entire change/feature, rather than having to "know" the range of commits to revert.
13. That's it, your changes have been merged! You will be given the option to delete your remote branch. but are not required to do so. We recommend it since it will keep your fork cleaner, but you can do whatever you like.

*Remember, code reviews can be tough. As a reviewer, it can be very tricky to give useful constructive criticism without coming off as condescending or degrading (emotions are hard to express through text!). As the recipient of a code review, it might feel like you are being criticized too harshly and that your hard work is being attacked. Remember that these are your teammates, who are not trying to arbitrarily devalue your contributions but are trying to help make the code as good as possible, for the good of the team.*

### Reviewing Pull Requests

When reviewing Pull Requests, it can be really difficult to phrase comments in a way that doesn't come across as aggressive or mean. That said, it's really important that we strive to keep Pull Requests friendly and open, both for the health of everyone involved, and the effectiveness of the code review process. Here are two links that everyone reviewing a pull request should _thoroughly_ read before doing reviews:

[https://mtlynch.io/human-code-reviews-1/](https://mtlynch.io/human-code-reviews-1/) 

[https://mtlynch.io/human-code-reviews-2/](https://mtlynch.io/human-code-reviews-2/)


## Example Workflow

We find our workflow is best explained by walking through an example. We're assuming you have already cloned the repository and set up your git remotes. If not, check out the [Getting the Code](#getting-the-code) instructions first and then come back.

This example incorporates information from the previous sections on [Issue and Project Tracking](#issue-and-project-tracking), and [the Git Workflow](#git-workflow). Make sure you have read those sections first. This example skips over some of the smaller details.
  
We are also assuming all the work done here is in your fork of the repository.

Let's pretend our goalie strategy isn't that great. You have noticed that and suggested we improve it. Here's what your workflow would likely look like, from start to finish. We will pretend your name is Bob.

1. Create a new Issue for the goalie strategy if it doesn't already exist
   1. Let's pretend this is `Issue #23`
   2. Add an estimated Difficulty tag to this issue
2. Create a new branch from `upstream/master`, called `bob/create_new_goalie_strategy`
   1. `git fetch upstream`
   2. `git checkout -b bob/create_new_goalie_strategy upstream/master`
3. Make your changes
   1. As you make changes and come across new information / challenges, it is good to update the Issue you are working on to document these new changes or requirements. Updating our progress on the ticket also helps other know how your work is going.
      1. `git commit -m "Improved the goalie's positioning during corner kicks, to block shots near the edge of the net"`
   2. Don't forget to push your changes to the branch on your fork occasionally, so you don't lose your work if something happens to your computer (it's happened to our team before)
4. Open a Pull Request to the master branch of the main Software repository. This will be a request to merge the branch `bob/create_new_goalie_strategy` from your fork, to the `master` branch of the main `Software` repository.
   1. The description should include `resolves #23`, so we know this Pull Request resolved your ticket
5. Discuss the changes with your reviewers and update the Pull Request by pushing additional commits to your branch
6. Once the Pull Request is approved and all CI checks pass, "Squash and merge" the changes
7. **Optional:** Delete your remote branch
8. Make sure your issue is marked as resolved. If you remembered to include `resolves #23` in your Pull Request description, this should have been done automatically for you, but it's good to double check.
9. Congratulations, you've now made changes to our main codebase!

## Testing

Testing is an integral part of our development process. If you are writing basically **any** code, it should be tested. If you feel like you can't test your piece of code, it's likely because it was written in a way that makes it difficult to test (which is a strong indicator for other problems, such as too much [coupling](https://en.wikipedia.org/wiki/Coupling_%28computer_programming%29)). _(An exception to this rule is any code that talks **directly** with hardware)_. For some examples of what happens when people don't test their code enough, see [here](https://web.archive.org/web/20201111163333/https://outfresh.com/knowledge-base/6-famous-software-disasters-due-lack-testing/). How to run tests is explained in the [Building and Running Code](#building-and-running-the-code) section. 

