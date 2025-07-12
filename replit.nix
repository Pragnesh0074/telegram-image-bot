{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.virtualenv
    pkgs.cacert
    pkgs.git
    pkgs.ffmpeg
    pkgs.libjpeg
    pkgs.zlib
  ];
} 