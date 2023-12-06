{ pkgs ? import <nixpkgs> {} }: pkgs.mkShell {
    packages = with pkgs; [
        (python3.withPackages (pip: [
            (pip.pygame.overrideAttrs {
                env.PYGAME_DETECT_AVX2 = "y";
            })
        ]))
    ];
}
