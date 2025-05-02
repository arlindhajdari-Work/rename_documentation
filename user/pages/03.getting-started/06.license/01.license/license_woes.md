---
title: 'License Woes'
metadata:
    description: 'Documentation woes.'
    author: 'Joe Bordes'
content:
    items:
        - '@self.children'
    limit: 5
    order:
        by: date
        dir: desc
    pagination: true
    url_taxonomy_filters: true
taxonomy:
    category:
        - development
    tag:
        - license
---

## coreBOS

coreBOS is distributed under [VPL 1.1 license](../02.vpl11). This is a modified [MPL 1.1 license](http://www.mozilla.org/MPL/1.1/annotated/) which is a business-friendly, Apache or MIT like license.

===

Some of our other extensions and modules follow a more limited [Vizsage License](../03.vizsage).

## Licenses

- [Vtiger Public License Version 1.1](../02.vpl11)
- [MPL 1.1 Annotated](http://www.mozilla.org/MPL/1.1/annotated/)
  - We believe wholeheartedly in the benefits of open source development, but not everyone does. Some people or groups may try to take advantage of the work of open source development through claims of patent infringement. This is unfortunate, but it is also reality. We suggest that you be aware of the intellectual property implications of what you are working on to protect yourself and others from falling afoul of someone else's patent.
- [MPL Explained](http://www.eionet.europa.eu/software/licenseexplained.html)
  - It is possible for you to compile and package the source code standalone or bundled with proprietory code as part of a larger work and sell it for profit. You may want to do this to provide a product warranty. But, you must tell the licensee that the source code to the part of the work is available and that vtiger nor any contributor accepts any liability for the malfunction of the code. (MozPL Section 3.6)
  - Coverage is on the source file level. Meaning: If you add a source file to the codebase, that file is owned by you, and you decide what license to use. But it must be possible to compile the product without that source file. If you modify a file already in the codebase the file continues to be under MozPL, and you must make the file available as open source.
- **vtiger CRM 6.0** is distributed under **VPL 1.2**. The only difference is that vtiger protects its trademark and logo.
- [GPL-Incompatible Free Software Licenses](http://www.gnu.org/licenses/license-list.en.html#MPL)
  - it has some complex restrictions that make it incompatible with the GNU GPL. That is, a module covered by the GPL and a module covered by the MPL cannot legally be linked together. We urge you not to use the MPL 1.1 for this reason.
  - However, MPL 1.1 has a provision (section 13) that allows a program (or parts of it) to offer a choice of another license as well. If part of a program allows the GNU GPL as an alternate choice, or any other GPL-compatible license as an alternate choice, that part of the program has a GPL-compatible license.
- [Combining MPL-Licensed files with an (L)GPL-Licensed Project: Guidelines for Developers](http://www.mozilla.org/MPL/2.0/combining-mpl-and-gpl.html)
  - **Unmodified MPL-licensed Files - MPL-only** In the simplest case, the developer combines unmodified MPL-licensed files into a project with (L)GPL-licensed files to create a Larger Work and seeks to distribute the resulting combination under the terms of the (L)GPL.
  - In this case, Section 3.3 of the MPL permits the individual files to be distributed as part of the Larger Work, with no further changes required. The developer may simply leave the file untouched, with all notices intact.
- [MPL / GPL Incompatibility](http://www.tomhull.com/ocston/docs/mozgpl.html)
- [OSI](http://opensource.org)
- [Vizsage License](../03.vizsage)
- [Evolutivo License](../04.evolutivo)
- [Business Source License](https://mariadb.com/bsl11/)
- [Fair-code is not a software license](https://faircode.io)
- [Fair Source License](https://fair.io/?a)
- [Server Side Public License (SSPL)](https://www.mongodb.com/licensing/server-side-public-license)
- [Open Source Eventually License](https://github.com/ftrotter/OSE)
- [GNU free documentation license](../../../09.security-guide/LicenseUsageAcknowledgements#gnu_free_documentation_license)

![VPL 1.1 Definitions](vpl1.1_definitions.png?width=450px)

[VPL 1.1 Definitions ODG](../02.vpl11/vpl1.1_definitions.odg)

## My understanding of the License

- Initial developer permits us to do whatever we want with the code: use it, sell it, rebrand it, modify it, but always under the same conditions of the license
- Contributor permits us to do whatever we want with their MODIFICATIONS: use them, sell them, rebrand them, modify them, but always under the same conditions of the license
- since both previous points impose that the user MUST not suffer any change in their liberties. This point makes it incompatible for the MODIFICATIONS to have a GPL license because the whole work would be affected
- we HAVE THE OBLIGATION of giving ALL our MODIFICATIONS in source code, we can not encrypt them nor change their license
- if we do a larger work, the VPL code described above cannot be restricted, in other words, anybody MUST have access to the original code and ALL its MODIFICATIONS
- we MUST detail all code modifications
- the code can be dual-licensed but only vtiger can do that
- "Modifications" This is a very important definition, as it specifies precisely what code you write must be made available and what you can keep proprietary.
  - Anything termed a "Modification" must be made available in source code form to anyone to whom you give a binary. The following defines a Modification:
    - If you change anything within one of the files contained in the Source Code, that is a Modification.
    - If you take code out of one of the files contained in the Source Code and place it in a new file, whether you add new code or not, that is a Modification.
    - If you rename a file or combine two or more files contained in the Source Code, that is a Modification.
