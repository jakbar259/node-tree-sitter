{
  "targets": [
    {
      "target_name": "tree_sitter_runtime_binding",
      "dependencies": ["tree_sitter"],
      "sources": [
        "src/binding.cc",
        "src/conversions.cc",
        "src/language.cc",
        "src/logger.cc",
        "src/node.cc",
        "src/parser.cc",
        "src/query.cc",
        "src/tree.cc",
        "src/tree_cursor.cc",
        "src/util.cc",
      ],
      "include_dirs": [
        "vendor/tree-sitter/lib/include",
        "vendor/superstring",
        "<!(node -e \"require('nan')\")",
      ],
      'conditions': [
        ['OS == "mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.9',
          },
        }],
        ['OS == "win"', {
          "msvs_settings": {
            "VCCLCompilerTool": {
              "AdditionalOptions": ["/std:c++17"]
            }
          },
          "msbuild_settings": {
            "ClCompile": {
              "LanguageStandard": "stdcpp17"
            }
          }
        }]
      ],
      "cflags_cc": [
        "-std=c++17",
        "-stdlib=libc++",
      ],
      'xcode_settings': {
        'CLANG_CXX_LANGUAGE_STANDARD': 'c++17',
      },
    },
    {
      "target_name": "tree_sitter",
      'type': 'static_library',
      "sources": [
        "vendor/tree-sitter/lib/src/lib.c"
      ],
      "include_dirs": [
        "vendor/tree-sitter/lib/src",
        "vendor/tree-sitter/lib/include",
      ],
      "cflags": [
        "-std=c99"
      ]
    }
  ],
  'variables': {
    'runtime%': 'node',
    'openssl_fips': '',
  },
  'conditions': [
      ['runtime=="electron"', { 'defines': ['NODE_RUNTIME_ELECTRON=1'] }],
  ]
}
