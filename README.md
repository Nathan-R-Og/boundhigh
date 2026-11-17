# Bound High!
Disassembly of Bound High! (Proto) for Virtual Boy.

While this game was 99% written in C, the original compiler `VUCC` doesn't work outside of a Windows environment. Until this gets fixed, this will be a purely assembly repository. Included will be C equivalents to functions, but no C will be bytematching due to how the different ABI works.

Currently only works on Linux Ubuntu. Could probably work on Windows, I'm just lazy.

## Supported Hashes
| Game Version                       | MD5                              |
|------------------------------------|----------------------------------|
| Bound High! (Proto)                |`a460e2660fa951e9d4e3b05aee9f5018`|

## Using
This project uses [v810-gcc](https://github.com/jbrandwood/v810-gcc) to compile, assemble and link. This project also uses the `ninja` build system.

The project was disassembled with the help of [v810_ds2](https://www.virtual-boy.com/tools/v810-disasm/) and it's source code.

1. Install `v810-gcc` and other dependencies by running `./install`. This will install `v810-gcc` at `tools/v810-gcc` as well as otehr python dependencies.

2. Place a Bound High! ROM in the root of the project. Name it `baserom.vb`.

3. Run `./configure` to split the ROM, convert assets to human formats and set up a ninja build script.

4. Run `ninja` to compile the project.

The output will be at `build/boundhigh.vb`.


## Project Directory:
`src/` - All source code files.

`include/` - All source code header files.

`reimplement/` - Source code assembly reinterpreted into C.

`build/` - Build output.

`split/` - Binary split from the game files.

`extract/` - Assets interpreted from the split game files.

`tools/` - Extraneous tools for development and reverse engineering.


