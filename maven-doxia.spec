%global pkg_name maven-doxia
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%if 0%{?fedora}
%bcond_without itext
%bcond_without markdown
%endif

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.4
Release:        5.13%{?dist}
Epoch:          0
Summary:        Content generation framework
License:        ASL 2.0
URL:            http://maven.apache.org/doxia/

Source0:        http://repo2.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip


# TODO: push upstream
# abstract class should not be annotated as component because maven
# will pick it up and try to instantiate
Patch1:         0001-doxia-core-remove-plexus-component-annotation.patch

Patch2:         0001-Update-to-Plexus-Container-1.5.5.patch

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}ant
BuildRequires:  maven30-plexus-cli
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-assembly-plugin
BuildRequires:  maven30-maven-compiler-plugin
BuildRequires:  maven30-maven-install-plugin
BuildRequires:  maven30-maven-jar-plugin
BuildRequires:  maven30-maven-javadoc-plugin
BuildRequires:  maven30-maven-resources-plugin
BuildRequires:  maven30-maven-plugin-plugin
BuildRequires:  maven30-maven-site-plugin
BuildRequires:  maven30-maven-shade-plugin
BuildRequires:  maven30-maven-surefire-plugin
BuildRequires:  maven30-maven-reporting-impl
BuildRequires:  maven30-maven-doxia-sitetools
BuildRequires:  maven30-maven-doxia-tools
BuildRequires:  maven30-modello
BuildRequires:  maven30-plexus-classworlds
BuildRequires:  %{?scl_prefix_java_common}apache-commons-collections
BuildRequires:  %{?scl_prefix_java_common}apache-commons-logging
BuildRequires:  maven30-apache-commons-validator
BuildRequires:  maven30-apache-commons-configuration
BuildRequires:  %{?scl_prefix_java_common}junit
BuildRequires:  %{?scl_prefix_java_common}jakarta-oro
BuildRequires:  maven30-plexus-i18n
BuildRequires:  maven30-plexus-utils
BuildRequires:  maven30-plexus-velocity
BuildRequires:  maven30-plexus-build-api
BuildRequires:  maven30-velocity
BuildRequires:  maven30-fop
BuildRequires:  maven30-plexus-containers-component-metadata
BuildRequires:  maven30-plexus-containers-component-javadoc
BuildRequires:  maven30-plexus-containers-container-default
BuildRequires:  %{?scl_prefix_java_common}httpcomponents-client
BuildRequires:  maven30-httpcomponents-project
BuildRequires:  maven30-xmlgraphics-commons
BuildRequires:  maven30-avalon-framework
BuildRequires:  maven30-geronimo-parent-poms
BuildRequires:  maven30-geronimo-jms
BuildRequires:  %{?scl_prefix_java_common}javamail
%if %{with itext}
BuildRequires:  maven30-itext
%endif
%if %{with markdown}
BuildRequires:  maven30-pegdown
%endif



%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.


%package core
Summary: Core module for %{pkg_name}

%description core
This package provides %{summary}.

%package logging-api
Summary: Logging-api module for %{pkg_name}

%description logging-api
This package provides %{summary}.

%package module-apt
Summary: APT module for %{pkg_name}

%description module-apt
This package provides %{summary}.

%package module-confluence
Summary: Confluence module for %{pkg_name}

%description module-confluence
This package provides %{summary}.

%package module-docbook-simple
Summary: Simplified DocBook module for %{pkg_name}

%description module-docbook-simple
This package provides %{summary}.

%package module-fml
Summary: FML module for %{pkg_name}

%description module-fml
This package provides %{summary}.

%package module-fo
Summary: FO module for %{pkg_name}

%description module-fo
This package provides %{summary}.

%if %{with itext}
%package module-itext
Summary: iText module for %{pkg_name}

%description module-itext
This package provides %{summary}.
%endif

%if %{with markdown}
%package module-markdown
Summary: Markdown module for %{pkg_name}

%description module-markdown
This package provides %{summary}.
%endif

%package module-latex
Summary: Latex module for %{pkg_name}

%description module-latex
This package provides %{summary}.

%package module-rtf
Summary: RTF module for %{pkg_name}

%description module-rtf
This package provides %{summary}.

%package modules
Summary: Doxia modules for several markup languages.

%description modules
This package provides %{summary}.

%package module-twiki
Summary: TWiki module for %{pkg_name}

%description module-twiki
This package provides %{summary}.

%package module-xdoc
Summary: XDoc module for %{pkg_name}

%description module-xdoc
This package provides %{summary}.

%package module-xhtml
Summary: XHTML module for %{pkg_name}

%description module-xhtml
This package provides %{summary}.

%package sink-api
Summary: Sink-api module for %{pkg_name}

%description sink-api
This package provides %{summary}.

%package tests
Summary: Tests for %{pkg_name}

%description tests
This package provides %{summary}.

%package test-docs
Summary: Test-docs module for %{pkg_name}

%description test-docs
This package provides %{summary}.

%package javadoc
Summary: Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n doxia-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%patch1 -p1
%patch2 -p1

# we don't have clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin pom.xml

# use java 5 generics in modello plugin
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='modello-maven-plugin']]"\
"/pom:executions/pom:execution/pom:configuration" \
"<useJava5>true</useJava5>" doxia-modules/doxia-module-fml/pom.xml

%mvn_package :::tests: tests

%if %{without itext}
%pom_disable_module doxia-module-itext doxia-modules
%endif
%if %{without markdown}
%pom_disable_module doxia-module-markdown doxia-modules
%endif
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
# tests disabled because some use old plexus-container and don't work
# with new
%mvn_build -s
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles-doxia
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE
%files core -f .mfiles-doxia-core
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files logging-api -f .mfiles-doxia-logging-api
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE
%files module-apt -f .mfiles-doxia-module-apt
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-confluence -f .mfiles-doxia-module-confluence
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-docbook-simple -f .mfiles-doxia-module-docbook-simple
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-fml -f .mfiles-doxia-module-fml
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-fo -f .mfiles-doxia-module-fo
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%if %{with itext}
%files module-itext -f .mfiles-doxia-module-itext
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%endif
%if %{with markdown}
%files module-markdown -f .mfiles-doxia-module-markdown
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%endif
%files module-latex -f .mfiles-doxia-module-latex
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-rtf -f .mfiles-doxia-module-rtf
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files modules -f .mfiles-doxia-modules
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-twiki -f .mfiles-doxia-module-twiki
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-xdoc -f .mfiles-doxia-module-xdoc
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files module-xhtml -f .mfiles-doxia-module-xhtml
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files sink-api -f .mfiles-doxia-sink-api
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files test-docs -f .mfiles-doxia-test-docs
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%files tests -f .mfiles-tests
%dir %{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE
%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 0:1.4-5.13
- maven33 rebuild

* Thu Jan 15 2015 Michael Simacek <msimacek@redhat.com> - 0:1.4-5.12
- All subpackages should own the shared directory

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.11
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 0:1.4-5.10
- Mass rebuild 2015-01-13

* Mon Jan 12 2015 Michael Simacek <msimacek@redhat.com> - 0:1.4-5.9
- Rebuild to regenerate requires from java-common

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 0:1.4-5.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.4
- Remove requires on java

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-5.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 01.4-5
- Mass rebuild 2013-12-27

* Thu Nov  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-4
- Package doxia-core test JAR

* Wed Nov  6 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-3
- Enable tests

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.4-2
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Michal Srb <msrb@redhat.com> - 0:1.4-1
- Update to upstream version 1.4
- Enable markdown module
- Remove unneeded patch

* Tue Apr 23 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.3-3
- Remove ant-nodeps BuildRequires

* Mon Apr  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.3-2
- Conditionally disable itext module

* Tue Mar 19 2013 Michal Srb <msrb@redhat.com> - 0:1.3-1
- Update to upstream version 1.3
- Remove temporary dependencies on subpackages

* Thu Feb  7 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-9
- Remove runtime requirement on POM: httpcomponents-project

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.2-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Dec 20 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.2-8
- Add httpcomponents-project to doxia-core requires

* Thu Dec 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2-7
- Temporarly require all subpackages in the main package

* Wed Dec 19 2012 Michal Srb <msrb@redhat.com>
- Splitted into multiple subpackages (Resolves: #888710)

* Mon Dec 10 2012 Michal Srb <msrb@redhat.com> - 0:1.2-5
- Migrated to plexus-components-component-default (Resolves: #878553)
- Removed custom depmap and its occurrence in spec file
- Fixed various rpmlint warnings

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan  9 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.2-3
- Remove plexus-xmlrpc from BR
- Update patches to work without plexus-maven-plugin

* Fri May  6 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.2-2
- Add forgotten missing requires

* Fri May  6 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.2-1
- Update to latest upstream (1.2)
- Use maven 3 to build
- Remove version limits on BR/R (not valid anymore anyway)
- Remove "assert" patch (no explanation for it's existence)

* Tue Feb 22 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1.4-3
- Change oro to jakarta-oro in BR/R

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 23 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1.4-1
- Update to 1.1.4
- Migrate from tomca5 to tomca6
- Versionless jars and javadocs
- Remove old skip-plugin patch
- Replace add-default-role-hint patch with remove-plexus-component patch
- Rename few jakarta BRs/Rs to apache names

* Tue Sep  7 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1.3-1
- New bugfix version
- Fix javadoc generation error
- Use %%{_mavenpomdir} macro
- Update BRs to latest maven plugin names
- Use new plexus-containers components
- Remove/update old patches

* Tue May 25 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.1.2-3
- Update for transitional maven state.
- Install doxia-modules pom.

* Wed May  5 2010 Mary Ellen Foster <mefoster at gmail.com> 0:1.1.2-2
- Add BuildRequirement on fop

* Fri Feb 12 2010 Mary Ellen Foster <mefoster at gmail.com> 0:1.1.2-1
- Update to 1.1.2
- Add update_maven_depmap to post and postun
- Temporarily disable javadoc until maven2-plugin-javadoc is rebuilt against
  the new doxia

* Mon Dec 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.8.a10.4
- BR maven2-plugin-plugin.

* Mon Dec 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.8.a10.3
- BR maven2-plugin-assembly.

* Mon Dec 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-0.8.a10.2
- BR maven-surefire-provider-junit.

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 0:1.0-0.8.a10.1
- Add tomcat5 BR

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 0:1.0-0.8.a10
- Add tomcat5-servlet-2.4-api BR

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 0:1.0-0.7.a10
- Fix plexus-cli BR version

* Mon Aug 31 2009 Andrew Overholt <overholt@redhat.com> 0:1.0-0.6.a10
- Add itext and plexus-cli BRs

* Wed Aug 26 2009 Andrew Overholt <overholt@redhat.com> 0:1.0-0.5.a10
- Update to 1.0 alpha 10 courtesy of Deepak Bhole
- Remove gcj support
- Add patch to build against iText 2.x (with back-ported XML classes)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.a7.2.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.a7.2.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 13 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.2.a7.2.10
- Fix broken release tag

* Wed Aug 13 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.2.a7.2.9
- Build for ppc64

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.2.a7.2.8
- drop repotag

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.2.a7.2jpp.7
- fix license tag

* Thu Feb 28 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.2.a7.2jpp.6
- Rebuild

* Fri Sep 21 2007 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a7.3jpp.5
- Build with maven
- ExcludeArch ppc64

* Sat Sep 01 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.a7.3jpp.4
- Rebuild without maven (fpr initial ppc build)

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.a7.3jpp.3
- Added switch to ignore failures for the time being

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.a7.3jpp.2
- Build with maven

* Tue Feb 27 2007 Tania Bento <tbento@redhat.com> 0:1.0-0.1.a7.3jpp.1
- Fixed %%Release.
- Fixed %%BuildRoot.
- Removed %%Vendor.
- Removed %%Distribution.
- Removed %%post and %%postun sections for javadoc.
- Fixed instructios on how to generate source drop.
- Fixed %%Summary.
- Added gcj support option.
- Marked configuration file as %%config(noreplace) in %%files section.

* Tue Oct 17 2006 Deepak Bhole <dbhole@redhat.com> 1.0-0.a7.3jpp
- Update for maven2 9jpp

* Fri Jun 23 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.a7.2jpp
- Fix versions in the depmap

* Wed Mar 15 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.a7.1jpp
- Initial build
