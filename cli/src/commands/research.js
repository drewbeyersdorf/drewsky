import inquirer from 'inquirer';
import chalk from 'chalk';
import fs from 'fs-extra';
import ora from 'ora';
import boxen from 'boxen';
import { generateResearchDoc } from '../utils/tcrei.js';
import { updateMetrics } from '../utils/file-helpers.js';

export async function researchCommand(task) {
  console.log(chalk.blue.bold('\n🔍 drewsky Research - TCREI Validation\n'));

  // Check if .drewsky exists
  if (!await fs.pathExists('.drewsky')) {
    console.log(chalk.red('❌ drewsky not initialized'));
    console.log(chalk.gray('   Run ') + chalk.cyan('drewsky init') + chalk.gray(' first'));
    console.log();
    process.exit(1);
  }

  console.log(chalk.gray('Answer these questions to validate your task:\n'));

  const answers = await inquirer.prompt([
    {
      type: 'input',
      name: 'task',
      message: chalk.cyan('Task:') + ' What exactly needs to be done?',
      default: task,
      validate: (input) => input.length > 0 || 'Task description is required'
    },
    {
      type: 'input',
      name: 'context',
      message: chalk.cyan('Context:') + ' Why is this needed? What problem does it solve?',
      validate: (input) => input.length > 0 || 'Context is required'
    },
    {
      type: 'input',
      name: 'reference',
      message: chalk.cyan('Reference:') + ' Any examples, docs, or patterns to follow?',
      default: 'None'
    },
    {
      type: 'input',
      name: 'evaluation',
      message: chalk.cyan('Evaluation:') + ' How will you measure success? What defines "done"?',
      validate: (input) => input.length > 0 || 'Evaluation criteria required'
    },
    {
      type: 'input',
      name: 'input',
      message: chalk.cyan('Input:') + ' What files/data/resources need to be examined?',
      validate: (input) => input.length > 0 || 'Input requirements needed'
    }
  ]);

  const spinner = ora('Generating research document...').start();

  try {
    // Generate research document
    const researchDoc = generateResearchDoc(answers);
    await fs.writeFile('.research.md', researchDoc);

    // Update metrics
    await updateMetrics({
      researchPhases: 1
    });

    spinner.succeed(chalk.green('Research document created'));

    console.log();
    console.log(boxen(
      chalk.green.bold('✅ TCREI Validation Complete\n\n') +
      chalk.white('Created: ') + chalk.cyan('.research.md') + '\n\n' +
      chalk.gray('Task:\n  ') + chalk.white(answers.task) + '\n\n' +
      chalk.gray('Context:\n  ') + chalk.white(answers.context) + '\n\n' +
      chalk.blue.bold('Next step:\n  ') +
      chalk.cyan('drewsky plan') + chalk.gray(' - Create implementation plan'),
      {
        padding: 1,
        margin: 1,
        borderStyle: 'round',
        borderColor: 'green'
      }
    ));

    console.log(chalk.gray('\n💡 Tip: Review .research.md before planning\n'));

  } catch (error) {
    spinner.fail(chalk.red('Failed to create research document'));
    console.error(chalk.red(`\nError: ${error.message}`));
    process.exit(1);
  }
}
