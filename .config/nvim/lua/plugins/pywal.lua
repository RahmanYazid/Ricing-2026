return {
  -- Pywal colorscheme
  {
    "AlphaTechnolog/pywal.nvim",
    lazy = false,
    priority = 1000,
    config = function()
      vim.cmd("colorscheme pywal")
    end,
  },

  -- Transparent background
  {
    "xiyaowong/transparent.nvim",
    lazy = false,
    config = function()
      require("transparent").setup({
        extra_groups = {
          "NormalFloat",
          "NvimTreeNormal",
          "NvimTreeNormalNC",
          "TelescopeNormal",
          "TelescopeBorder",
          "WhichKeyFloat",
        },
      })
      require("transparent").clear_prefix("BufferLine")
      require("transparent").clear_prefix("lualine")
    end,
  },
}
