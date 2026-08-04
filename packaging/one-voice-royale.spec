%global debug_package %{nil}
%global __os_install_post %{nil}
%global _build_id_links none

Name:           one-voice-royale
Version:        1.3.92
Release:        1%{?dist}
Summary:        Mikrofoni -> Whisper -> kaannos -> puhesynteesi -sovellus
License:        Proprietary
URL:            https://github.com/JuhaFIN1/one-voice-royale
Source0:        one-voice-royale-%{version}-linux-x86_64.tar.gz
Source1:        one-voice-royale.desktop
Source2:        iconimage.png
BuildArch:      x86_64
AutoReqProv:    no
Requires:       mesa-libEGL, mesa-libGL, xcb-util-cursor, xcb-util-wm, xcb-util-keysyms, xcb-util-image, xcb-util-renderutil, libxkbcommon-x11, pipewire-pulseaudio, espeak-ng, ffmpeg-free
# Renamed from voice-royale (v1.3.91) — let dnf upgrade-in-place instead of leaving both installed
Obsoletes:      voice-royale < %{version}-%{release}
Provides:       voice-royale = %{version}-%{release}

%description
One Voice Royale: mikrofonista puhe tekstiksi (Whisper), kaannos (Google/DeepL/OpenAI)
ja puhesynteesi (ElevenLabs/Edge TTS/OpenAI). Fedora Linux -kannettava paketti,
sisaltaa oman Python-runtimen (PyInstaller onedir-build), ei ulkoisia
pip-riippuvuuksia asennushetkella.

%prep
%setup -q -c -n one-voice-royale-src

%build
# no build step, binary is pre-built by PyInstaller

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/one-voice-royale
cp -a one-voice-royale/. %{buildroot}/opt/one-voice-royale/
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/one-voice-royale.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/one-voice-royale.png
mkdir -p %{buildroot}%{_bindir}
ln -sf /opt/one-voice-royale/one-voice-royale %{buildroot}%{_bindir}/one-voice-royale

%files
/opt/one-voice-royale
%{_bindir}/one-voice-royale
%{_datadir}/applications/one-voice-royale.desktop
%{_datadir}/icons/hicolor/256x256/apps/one-voice-royale.png

%post
/usr/bin/update-desktop-database &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%postun
/usr/bin/update-desktop-database &>/dev/null || :

%changelog
* Tue Aug 04 2026 BluexDEV Softwares <asiakaspalvelu@selaa.fi> - 1.3.92-1
- Nimenmuutos: voice-royale -> one-voice-royale (Obsoletes/Provides varmistaa dnf-paivityksen)
* Thu Jul 23 2026 BluexDEV Softwares <asiakaspalvelu@selaa.fi> - 1.3.91-1
- Ensimmainen Fedora Linux -porttaus (PyInstaller onedir + RPM)
