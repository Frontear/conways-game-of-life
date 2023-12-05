{ pkgs ? import <nixpkgs> {} }: pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
        python311Full
        python311Packages.pygame
    ];
}
