{ pkgs }: {
  deps = [
    pkgs.python311Packages.flake8
    pkgs.python310Packages.flake8
  ];
}