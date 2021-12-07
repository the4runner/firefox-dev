%global             source_name firefox
%global             application_name firefox-dev

Name:               firefox-dev
Version:            96.0b1
Release:            1%{?dist}
Summary:            Firefox Developer Edition (formerly "Aurora") pre-beta Web browser

License:            MPLv1.1 or GPLv2+ or LGPLv2+
URL:                https://www.mozilla.org/en-US/firefox/developer/
Source0:            https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version}/linux-x86_64/en-US/firefox-%{version}.tar.bz2
Source1:            firefox-developer-edition.desktop

ExclusiveArch:      x86_64

Requires(post):     xdg-utils
Requires(post):     gtk-update-icon-cache

%description
This is a pre-beta release of Mozilla Firefox intended for Web developers and
enthusiasts who want early access to new features. It receives new updates
(almost) daily, adding and refining support for the very latest Web standards
that won't make it into the stable release of Firefox for some months. It also
comes with some addons for Web development enabled by default.

You may actually find that Developer Edition works just fine for normal everyday
use: Some users set it as their default Web browser. You can sign in to your
normal Firefox account and sync your preferences, extensions, and bookmarks,
etc. Or you can keep the Firefox versions separate, and use different profiles,
even different browser UI themes. Firefox Developer Edition can install
alongside the stable release of Firefox, making it easy to switch back and forth
between the two versions.

That being said, a lot of the technology here is still experimental, and there
will very likely be some bugs, so just remember that by using Developer Edition,
you're helping Mozilla make Firefox the best Web browser they can. And have fun!

Bugs related to Firefox Developer Edition should be reported directly to Mozilla: 
<https://bugzilla.mozilla.org/>

Bugs related to this package should be reported at this GitHub project:
<https://github.com/the4runner/firefox-dev/issues/>

%prep
%setup -q -n %{source_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{application_name},%{_bindir},%{_datadir}/applications}

%__cp -r * %{buildroot}/opt/%{application_name}

%__ln_s /opt/%{application_name}/firefox %{buildroot}%{_bindir}/%{application_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%post
xdg-icon-resource install --novendor --size 128 /opt/firefox-dev/browser/chrome/icons/default/default128.png firefox-developer-edition
gtk-update-icon-cache -f -t /usr/share/icons/hicolor

%files
%{_datadir}/applications/firefox-developer-edition.desktop
%{_bindir}/%{application_name}
/opt/%{application_name}

%changelog
* Tue Dec 7 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 96.0b1
- Minor version upgrade

* Fri Nov 26 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 95.0b12
- Minor version upgrade

* Wed Nov 24 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 95.0b11
- Minor version upgrade

* Wed Nov 24 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 95.0b10
- Minor version upgrade

* Fri Nov 19 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 95.0b9
- Minor version upgrade

* Wed Nov 17 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 95.0b8
- Minor version upgrade

* Mon Nov 15 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 95.0b7
- Minor version upgrade

* Sun Nov 14 2021 Anjalo Hettiarachchi <anjalohettiarachchi@gmail.com> - 95.0b6
- Initial build