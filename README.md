# firefox-dev
![OGImage](https://res.cloudinary.com/axicon/image/upload/c_scale,w_800/v1636892734/GitHub/AnjaloHettiarachchi/firefox-dev/github-og-template-01_mbggye.png "the4runner/firefox-dev")

[![Powered By: Copr](https://img.shields.io/badge/Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
![Arch: x86_64](https://img.shields.io/badge/Arch-x86__64-blue?style=flat-square)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/the4runner/firefox-dev/package/firefox-dev/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/the4runner/firefox-dev/package/firefox-dev/)

An unofficial RPM package of [Firefox Developer Edition](https://www.mozilla.org/en-US/firefox/developer) designed for [Fedora](https://getfedora.org).

## ⚠️ Special Note
This is just an RPM packaging for the said software and does not include any licenses of its own. The only additional file included is the `.desktop` file written based on the original executable from the Firefox Release Channel (default).

## About the Application
This is a pre-beta release of Mozilla Firefox intended for Web developers and
enthusiasts who want early access to new features. It receives new updates
(almost) daily, adding and refining support for the very latest Web standards
that won't make it into the stable release of Firefox for some months. It also
comes with some addons for Web development enabled by default.

You may find that Developer Edition works just fine for everyday
use: Some users set it as their default Web browser. You can sign in to your
normal Firefox account and sync your preferences, extensions, and bookmarks,
etc. Or you can keep the Firefox versions separate, and use different profiles,
even different browser UI themes. Firefox Developer Edition can install
alongside the stable release of Firefox, making it easy to switch back and forth
between the two versions.

That being said, a lot of the technology here is still experimental, and there
will very likely be some bugs, so just remember that by using Developer Edition,
you're helping Mozilla make Firefox the best Web browser they can. And have fun!

Bugs related to Firefox Developer Edition should be reported directly to Mozilla: [https://bugzilla.mozilla.org](https://bugzilla.mozilla.org)

Bugs related to this package should be reported at this GitHub project:
[https://github.com/the4runner/firefox-dev/issues](https://github.com/the4runner/firefox-dev/issues)

## Installation Instructions
1. Enable `the4runner/firefox-dev` [Copr](https://copr.fedorainfracloud.org/) repository according to your package manager.

```Shell
# If you are using dnf... (you need to have 'dnf-plugins-core' installed)
sudo dnf copr enable the4runner/firefox-dev

# If you are using yum... (you need to have 'yum-plugins-copr' installed)
sudo yum copr enable the4runner/firefox-dev
```

2. (Optional) Update your package list.

```Shell
sudo dnf check-update
```

3. Execute the following command to install the package.

```Shell
sudo dnf install firefox-dev
```

4. Launch the application from the Application Menu or execute following command in terminal.

```Shell
firefox-dev
```
